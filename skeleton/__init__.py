# this is a marker file,its *existence* is necessary, but its content isn't
# In this minimal example I choose to re-export the main function
# to allow external usage as `from skeleton import main` (which is meant to be used in tests)

from skeleton.__main__ import main
