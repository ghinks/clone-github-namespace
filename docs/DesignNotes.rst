Design Notes
==========

Repo structure
------------

Introduce module methodology
------------------------------
Namespace packages or setuptools entry points


Query github to get all the repos in a organization.
------------
Query the organization and collect the repository data. This will need the
choice of a suitable graphQL library interface.


Take argument for workspace/organization name.
--------------
Take input file for defined list of repos to clone (feature)
--------------------
Clone defined and state which ones were not cloned too.

Introduce unit testing methodology
------------------------------
Pytest has been choosen as the test too.

CI/CD integration with the github actions
----------------------------------------

Is it possible to detect if the ssh key is valid for the org?
-------------------------------------------------------

Not running from main.py due to imports
--------------------------------------------------