from ibm1 import IBM1

class IBM1_add0(IBM1):

  def __init__(self, e_vocab, f_vocab, multiplier = 2):
    IBM1.__init__(self, e_vocab, f_vocab)
    self.multiplier = multiplier

  def _update_parameters(self, params, joint_expectations, expectations):
    for e in expectations:
      expectation_e = expectations[e]
      joint_expectations_e = joint_expectations[e]
      multiplier = 1
      if e == self.null_word:
        multiplier = self.multiplier
      for f in joint_expectations_e:
        params[f][e] = multiplier * (joint_expectations_e[f] / expectation_e)
