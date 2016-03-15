#include <vector>
#include <iostream>
#include <fstream>
#include <string>

#include "ChipaFF.h"
#include "moses/ScoreComponentCollection.h"
#include "moses/TargetPhrase.h"

using namespace std;

namespace Moses {
ChipaFF::ChipaFF(const std::string &line) : StatelessFeatureFunction(2, line) {
  ReadParameters();
}


const string SERVER_TO_CLIENT_PATH = "/tmp/server_to_client.fifo";
const string CLIENT_TO_SERVER_PATH = "/tmp/client_to_server.fifo";

// TODO(alexr): going to need to understand how to use this input object and
// what we want to feed back into Moses.
double makeRpcCall(const InputType &input) {
  std::ofstream c2s;
  c2s.open(CLIENT_TO_SERVER_PATH.c_str());
  c2s << s;
  c2s.close();

  // Read response from server's output fifo.
  string response;
  std::ifstream s2c(SERVER_TO_CLIENT_PATH.c_str());
  std::getline(s2c, response);
  s2c.close();

  double out = std::stod(response);

  return out;
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
