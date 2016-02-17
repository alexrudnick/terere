#include <vector>

#include <xmlrpc-c/girerr.hpp>
#include <xmlrpc-c/base.hpp>
#include <xmlrpc-c/client_simple.hpp>

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

// TODO(alexr): going to need to understand how to use this input object and
// what we want to feed back into Moses.
double makeRpcCall(const InputType &input) {

    double sum;
    try {
        string const serverUrl("http://localhost:8080/RPC2");
        string const methodName("sample.add");

        xmlrpc_c::clientSimple myClient;
        xmlrpc_c::value result;
        
        myClient.call(serverUrl, methodName, "ii", &result, 5, 7);

        // XXX: how do we get more complex types out? I guess we just need a
        // float back, really.
        // Assume the method returned a double; throws error if not
        sum = xmlrpc_c::value_double(result);
        cout << "Result of RPC (sum of 5 and 7): " << sum << endl;

    } catch (exception const& e) {
        cerr << "Client threw error: " << e.what() << endl;
        exit(1);
    }
  return sum;
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
