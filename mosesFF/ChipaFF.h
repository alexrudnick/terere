#pragma once

#include <string>
#include "StatelessFeatureFunction.h"

namespace Moses {

class ChipaFF : public StatelessFeatureFunction {
 public:
  ChipaFF(const std::string &line);

  bool IsUseable(const FactorMask &mask) const { return true; }

  void EvaluateWithSourceContext(
      const InputType &input, const InputPath &inputPath,
      const TargetPhrase &targetPhrase, const StackVec *stackVec,
      ScoreComponentCollection &scoreBreakdown,
      ScoreComponentCollection *estimatedScores = NULL) const;

  void EvaluateTranslationOptionListWithSourceContext(
      const InputType &input,
      const TranslationOptionList &translationOptionList) const;

  void EvaluateWhenApplied(const Hypothesis &hypo,
                           ScoreComponentCollection *accumulator) const;
  void EvaluateWhenApplied(const ChartHypothesis &hypo,
                           ScoreComponentCollection *accumulator) const;
};
}