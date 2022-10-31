test = {
  'name': 'Question 2_wbc_likely_normal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'wbc_likely_normal'
          >>> 'wbc_likely_normal' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'wbc_likely_normal'
          >>> # from its initial state (of ...)
          >>> wbc_likely_normal is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> wbc_likely_normal
          3
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
