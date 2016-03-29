#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <boost/algorithm/string/join.hpp>

#include "ChipaFF.h"
#include "moses/ScoreComponentCollection.h"
#include "moses/TargetPhrase.h"
#include "moses/InputType.h"
#include "moses/InputPath.h"

using namespace std;

namespace Moses {
ChipaFF::ChipaFF(const std::string &line) : StatelessFeatureFunction(1, line) {
  ReadParameters();
}


const string SERVER_TO_CLIENT_PATH = "/tmp/server_to_client.fifo";
const string CLIENT_TO_SERVER_PATH = "/tmp/client_to_server.fifo";

double makeRpcCall(const InputType& input,
                   const InputPath &inputPath,
                   const TargetPhrase& targetPhrase) {
  // Get the text out of the input sentence, put it into a single string.
  vector<string> tokens;
  vector<FactorType> factors;
  factors.push_back(0);
  for (unsigned int i = 0; i < input.GetSize(); ++i) {
    string word = input.GetWord(i).GetString(factors, false);
    tokens.push_back(word);
  }
  string sentence = boost::algorithm::join(tokens, " ");

  tokens.clear();
  for (unsigned int i = 0; i < targetPhrase.GetSize(); ++i) {
    string word = targetPhrase.GetWord(i).GetString(factors, false);
    tokens.push_back(word);
  }
  string translation = boost::algorithm::join(tokens, " ");

  size_t source_index = inputPath.GetWordsRange().GetStartPos();

  // going to send SOURCE_SENTENCE<tab>FOCUS_INDEX<tab>PROPOSED_TRANSLATION
  std::ofstream c2s;
  c2s.open(CLIENT_TO_SERVER_PATH.c_str());
  c2s << sentence << "\t" << source_index << "\t" << translation;
  c2s.close();

  // Read response from server's output fifo.
  string response;
  std::ifstream s2c(SERVER_TO_CLIENT_PATH.c_str());
  std::getline(s2c, response);
  s2c.close();

  std::string::size_type sz;
  double out = atof(response.c_str());

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

    newScores[0] = makeRpcCall(input, inputPath, targetPhrase);
    scoreBreakdown.PlusEquals(this, newScores);
  }
}

void ChipaFF::EvaluateInIsolation(
    const Phrase &source, const TargetPhrase &targetPhrase,
    ScoreComponentCollection &scoreBreakdown,
    ScoreComponentCollection &estimatedScores) const {
  // Can't really evaluate this in isolation.
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
