.. E-CEO Data Challenges platform documentation master file, created by
   sphinx-quickstart on Wed Mar 26 11:35:03 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Overview
========

.. toctree::
   :maxdepth: 2
   

Purpose of the software
-------------------------

The project addresses the technologies and architectures needed to
provide a collaborative research Platform for automating data mining and
information extraction experiments. The Platform serves for the
implementation of open challenges focusing on Information Extraction for
EO applications. The possibility to implement – through the challenges –
different approaches and algorithms in a common Software Environment
(provided by the collaborative Platform) facilitates the comparison and
the evaluation between different methodologies, which is one of the main
requirements requested by scientific experts who develop algorithms in
the EO field. The project objectives are to provide a collaborative
research Platform for:

- Automation of data mining and information extraction experiments
- Generation of reproducible results that can be easily shared
- Addressing specific scientific challenges and tackling new research problems in a “parallel and collaborative way”

The platform allows the set-up three on-line challenges, which can be
appealing way of conducting research in data mining.

The platform is composed of a front-end (GUI) and a back-end (webserver).

Challenges Phases
-----------------
A challenge (which is the core part of the portal) is divided into 6 phases:

- Challenge is under creation |image: challenge\_created.png|
- Challenge is visible |image: challenge\_promoted.png|
- Challenge is open to applications |image: challenge\_open.png|
- Challenge is In Progress |image: challenge\_in\_progress.png|
- Challenge is On Evaluation |image: challenge\_on\_evaluation.png|
- Challenge is Closed |image: challenge\_closed.png|


Phase 1 (Challenge created)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Challenge creation and definition
-  Challenge modification
-  Challenge promotion
-  Challenge users management
-  Series and data package management
-  Data package for challenge management
-  Challenge Environment management
-  Evaluation Criterion creation
-  Evaluation Tree management
-  Notifications cleaning

Phase 2 (Challenge visible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Challenge description can be accessed

Phase 3 (Challenge promoted)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Application to a challenge
-  User certificate upload
-  Challenge start
-  Challenge users management
-  Environment creation
-  Notifications cleaning

Phase 4 (Challenge started)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Participant Application status update (packaging)
-  Participant Application status update (validation)
-  Participant Application references update
-  Challenge stop
-  Notifications cleaning

Phase 5 (Challenge ended / on evaluation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Participant Application status update (evaluation)
-  Participant Application references update
-  Environment nodes scalability
-  Notifications cleaning

Phase 6 (Challenge closed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Challenge results are published and accessible.


Challenges User Roles
---------------------

The software can be use by 4 type of users: Participants, Initiators,
Evaluators, Administrators.

Challenge **participants** will use the platform to:

-  get information about a challenge,
-  get information about their Private Environment,
-  get support from the support team,
-  provide information about their application,
-  get application evaluation result

Challenge **initiators** will use the platform to:

-  define a challenge,
-  get challenge status and evolution,
-  accept or reject users for a challenge,
-  define data packages

Challenge **evaluators** will use the platform to:

-  define challenge evaluation tree,
-  evaluate participant application,
-  get information about the Evaluation Environment

Challenge **administrators** will use the platform to:

-  accept or reject users for a challenge,
-  set-up environments,
-  validate participant applications,
-  define data packages
