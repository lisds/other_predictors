test = {
  'name': 'Question q_11_mae_predictors',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'predictors'
          >>> 'predictors' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'predictors'
          >>> # from its initial state (of ...)
          >>> predictors is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose((predictors - 7000) * 2, np.arange(6000))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need to set the value for 'mae_for_predictors'
          >>> 'mae_for_predictors' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mae_for_predictors'
          >>> # from its initial state (of ...)
          >>> mae_for_predictors is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(mae_for_predictors) == len(predictors)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # This is a fancy "vectorized" method to do the calcuations,
          >>> # but you probably used a "for" loop.
          >>> my_wbc = np.array(ckd['White Blood Cell Count'])
          >>> ps = np.arange(6000) / 2 + 7000  # Slightly obfuscated.
          >>> m_abs_deviations = np.mean(np.abs(my_wbc[:, None] - ps), axis=0)
          >>> np.allclose(mae_for_predictors, m_abs_deviations)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
