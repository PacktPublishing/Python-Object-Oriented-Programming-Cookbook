# Creating the Python VE (if needed)

Because the default version of Python on the Author's system was in the 
2.7.x range, a Python Virtual Environment was created specifically 

## Linux instructions

-    Creating the virtual environment:

    `python3 -m venv ~/py_envs/pyoopc`

    > Or use whatever other path is convenient/preferred over the `py-envs` 
    > specified — whatever that path is, it would be needed in the activation 
    > command-line call, below, as well)

-    Activating the virtual environment:

    `source ~/py_envs/pyoopc/bin/activate`

-    Creating the virtual environment:

    `deactivate`

-   Updating the associated `requirements.txt` file:

    `pip freeze | grep -v ".*==0\.0\.0" > requirements.txt`

    > The `grep` removes any packages with malformed version metadata, 
    > which is a concern for any Ubuntu-based Linux distros — they tend to 
    > contain 

    > ```pkg-resources==0.0.0```

    > with some frequency

<!--
## Windows instructions

-    Creating the virtual environment:

    `[TBD]`

-    Activating the virtual environment:

    `[TBD]`

-    Creating the virtual environment:

    `[TBD]`

-->
