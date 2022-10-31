test = {
  'name': 'Question q_10_mae_func',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you remember to return a value from your function?
          >>> mean_abs_err(np.array([3, 5]), 5) is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mean_abs_err(np.array([3, 4]), 5) == 1.5
          True
          >>> mean_abs_err(np.array([3, 5]), 4) == 1
          True
          >>> np.isclose(mean_abs_err(np.array([2, 3, 5]), 4), 4/3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_wbc = ckd['White Blood Cell Count']
          >>> np.isclose(mean_abs_err(my_wbc, 10000),
          ...                        np.abs(my_wbc - 10000).mean())
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
