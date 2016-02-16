#include <vector>
#include <xmlrpc.h>
#include <xmlrpc_client.h>

#include "ChipaFF.h"
#include "moses/ScoreComponentCollection.h"
#include "moses/TargetPhrase.h"

using namespace std;

namespace Moses {
ChipaFF::ChipaFF(const std::string &line) : StatelessFeatureFunction(2, line) {
  ReadParameters();
}

#define NAME "XML-RPC for ChipaFF"
#define VERSION "0.1"
#define SERVER_URL "http://localhost:8000/"

void die_if_fault_occurred(xmlrpc_env *env) {
  /* Check our error-handling environment for an XML-RPC fault. */
  if (env->fault_occurred) {
    fprintf(stderr, "XML-RPC Fault: %s (%d)\n", env->fault_string,
            env->fault_code);
    exit(1);
  }
}

// TODO(alexr): going to need to understand how to use this input object and
// what we want to feed back into Moses.
float makeRpcCall(const InputType &input) {
  xmlrpc_env env;
  xmlrpc_value *result;
  xmlrpc_int32 sum, difference;

  /* Start up our XML-RPC client library. */
  xmlrpc_client_init(XMLRPC_CLIENT_NO_FLAGS, NAME, VERSION);
  xmlrpc_env_init(&env);

  /* Call our XML-RPC server. */
  result = xmlrpc_client_call(&env, SERVER_URL, "sample.sum_and_difference",
                              "(ii)", (xmlrpc_int32)5, (xmlrpc_int32)3);
  die_if_fault_occurred(&env);

  /* Parse our result value. */
  xmlrpc_parse_value(&env, result, "{s:i,s:i,*}", "sum", &sum, "difference",
                     &difference);
  die_if_fault_occurred(&env);

  /* Print out our sum and difference. */
  printf("Sum: %d, Difference: %d\n", (int)sum, (int)difference);

  /* Dispose of our result value. */
  xmlrpc_DECREF(result);

  /* Shutdown our XML-RPC client library. */
  xmlrpc_env_clean(&env);
  xmlrpc_client_cleanup();

  float output_sum = (float)sum;
  return output_sum;
}

void ChipaFF::EvaluateWithSourceContext(
    const InputType &input, const InputPath &inputPath,
    const TargetPhrase &targetPhrase, const StackVec *stackVec,
    ScoreComponentCollection &scoreBreakdown,
    ScoreComponentCollection *estimatedScores) const {
  // XXX need to find out what the current focus word is and how to get the
  // whole source sentence.

  if (targetPhrase.GetNumNonTerminals()) {
    vector<float> newScores(m_numScoreComponents);

    newScores[0] = makeRpcCall(input);
    scoreBreakdown.PlusEquals(this, newScores);
  }
}

void ChipaFF::EvaluateInIsolation(
    const Phrase &source, const TargetPhrase &targetPhrase,
    ScoreComponentCollection &scoreBreakdown,
    ScoreComponentCollection &estimatedScores) const {
  // dense scores
  vector<float> newScores(m_numScoreComponents);
  newScores[0] = 1.5;
  newScores[1] = 0.3;
  scoreBreakdown.PlusEquals(this, newScores);

  // sparse scores
  scoreBreakdown.PlusEquals(this, "sparse-name", 2.4);
}

void ChipaFF::EvaluateTranslationOptionListWithSourceContext(
    const InputType &input,
    const TranslationOptionList &translationOptionList) const {}

void ChipaFF::EvaluateWhenApplied(const Hypothesis &hypo,
                                  ScoreComponentCollection *accumulator) const {
}

void ChipaFF::EvaluateWhenApplied(const ChartHypothesis &hypo,
                                  ScoreComponentCollection *accumulator) const {
}
}
