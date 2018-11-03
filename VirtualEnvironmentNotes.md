# Creating the Python VE (if needed)

Because the default version of Python on the Author's system was in the 
2.7.x range, a Python Virtual Environment was created specifically to 
provide the most current version of Python that the upstream provider 
actively supports. Code written against this VE (virtual environment) is 
generally expected to work for later versions (3.7.x) as well, but if 
there are any known point where that will fail, they will be noted.

## Linux instructions

-    Creating the virtual environment (`pyoopc`):

    `python3 -m venv ~/py_envs/pyoopc`

    Or use whatever other path is convenient/preferred over the `py-envs` 
    specified — whatever that path is, it would be needed in the activation 
    command-line call, below, as well)

-    Activating the `pyoopc` virtual environment:

    `source ~/py_envs/pyoopc/bin/activate`

-    Deactivating the `pyoopc` virtual environment:

    `deactivate`

-   Updating the associated `requirements.txt` file:

    `pip freeze | grep -v ".*==0\.0\.0" > requirements.txt`

    The `grep` removes any packages with malformed version metadata, 
    which is a concern for any Ubuntu-based Linux distros — they tend to 
    contain 

    `pkg-resources==0.0.0`

    with some frequency

<!--
## Windows instructions

-    Creating the virtual environment:

    `[TBD]`

-    Activating the virtual environment:

    `[TBD]`

-    Creating the virtual environment:

    `[TBD]`

-->
