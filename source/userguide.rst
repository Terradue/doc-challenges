

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

The platform is composed of a front-end (GUI) and a back-end
(webserver).

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

External view of the software
-------------------------------

The file **'web.config'** (/usr/local/eceo/sites/eceo/root/config on the
server) contains a set of configuration values used by the server (such
as BaseUrl, database connection fields, ...).

The mysql database is called '**eceo**\ ' and contains all the tables
used by the system. The table **'config'** contains all configurable
values.

Operations environment
------------------------

General
~~~~~~~~~~~

The platform is installed on a server where both the front-end and
back-end part are installed.

Software configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Software configuration can be done by editing the file **'web.config'**
(/usr/local/eceo/sites/eceo/root/config on the server) or the table
**'config'** of the database **'eceo'**.

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

cf T2UK-ESA-ECEO-PR-13-053

Operational constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The machine hosting the webserver shall be accessible via a public IP.

Operations basics
-------------------

There are 4 types of users of the E-CEO portal :

-  Administrator
-  Initiator
-  Evaluator
-  Participant

We add to these types of user a 5th one which is the portal agent. The
portal agent is a daemon running in background and performing actions in
a cyclic way (for example, every hour the notifications are cleaned from
the database). All actions done by the agent are done automatically.
User may receive notifications about these actions.

The following are the basics operations done in the E-CEO portal. Note
that the Administrator will be able to proceed all actions supposed to
be done by the other type of users.

Challenge creation and definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Creation of the challenge and definition of the basic informations.

Challenge modification
~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Modification of the challenge information.

Challenge promotion
~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Validates the challenge definition and makes it available for application
by Participants.

Application to a challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Participant**

Apply to participate to a challenge.

Challenge start
~~~~~~~~~~~~~~~~~

**Portal Agent**

Update the status of the challenge. Make available all packages on the
environments.

Challenge stop
~~~~~~~~~~~~~~~~

**Portal Agent**

Update the status of the challenge. Participant cannot package new
Application.

Challenge users management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add new Initiator / Change challenge Initiator or Evaluator / Accept or
deny Participant for a challenge.

Series management
~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add new series in the database.

Data package management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Create new data packages from the series.

Data package for challenge management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Associate data package to a challenge.

Challenge Environment management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Choose template, provider and virtual network for a challenge. Create
environments

Environment creation
~~~~~~~~~~~~~~~~~~~~~~~~~

**Portal Agent / Administrator**

Automatic environment creation X days before the start of the challenge by
the portal agent. Administrator can choose to start mnually the
environments.

Participant Application status update (packaging)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Participant**

Set Application as packaged and available for validation.

Participant Application status update (validation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Validate the Application and set it as available for evaluation or
reject Application.

Participant Application status update (evaluation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Evaluator**

Evaluate Application (apply quantification and or normalization).

Participant Application references update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Portal Agent**

Look for new application packaged on the Common Environment and for new
application evaluated on the Evaluation Environment.

User certificate upload
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Participant**

Upload certificate on the platform to access Environments.

Evaluation Criterion creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add a new criterion or remove an existing one (new criteria are
available for all challenges).

Evaluation Tree management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Evaluator**

Associate a criterion to a challenge or remove a criterion from a challenge.

Notifications cleaning
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Portal Agent**

Remove all read notifications.

Environment nodes scalability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add or remove node to an environment.

Operations manual
-------------------

General
~~~~~~~~~~~

A challenge (which is the core part of the portal) is divided into 6
phases:

#. Challenge is under creation |image:
   challenge\_created.png|
#. Challenge is visible |image:
   challenge\_promoted.png|
#. Challenge is open to applications |image:
   challenge\_open.png|
#. Challenge is In Progress |image:
   challenge\_in\_progress.png|
#. Challenge is On Evaluation |image:
   challenge\_on\_evaluation.png|
#. Challenge is Closed |image:
   challenge\_closed.png|

Normal operations
~~~~~~~~~~~~~~~~~~~~~

See `Section 8 <#sec_Operations_basics>`__ for details about all listed
operations.

Phase 1 (Challenge created)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Challenge creation and definition
-  Challenge modification
-  Challenge promotion
-  Challenge users management (initiator/evaluator)
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
-  Challenge users management (participants)
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

Reference manual
-------------------

Introduction
~~~~~~~~~~~~~~~~~

Screen definitions and operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Home page

The home page of the E-CEO portal is as shown in the following figure.
It contains a top bar, which is an quick access to all type of challenge
of the portal:

-  My Challenges: the challenges I am involved in.
-  Join a Challenge: open or on-going challenges that a user can join.
-  Upcoming Challenges: future challenges that a user cannot yet join.
-  Past Challenges: closed challenges, only results are accessible.
-  Settings: functionalities only accessible for the administrator
-  User info: access to user information such as account, profile,
   support or help page.
-  Notifications: notifications of the logged user.

The menu bar is updated according to the user logged in (administrator
will have the Settings |image:
homepage.png|

Figure 1:

Home page

User infos
^^^^^^^^^^^^^^^^^

From any page, the user can access some infos related to him by clicking
on its name on the top bar.

|image:
user\_info.png|

Figure 2:

User infos

User profile (All users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From any page, the user can access its profile by clicking “\ **my
profile**\ ” from the top bar (user infos).

Here he can update its information such as email, affiliation, country,
redmine API Key (used to access support tickets) or to receive
notifications via emails.

To update the Redmin API key, the user must click on “\ **Modify
Account**\ ” and then set the new API key (can be found on the redmine
profile of the user).

|image:
user\_profile.png|

Figure 3:

User profile

User certificate (All users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From any page, the user can access its profile by clicking “\ **my**
**certificate”** from the top bar (user infos).

Here he can ask for a new certificate or upload the one he has. The
certificate is the one used to access the Private Environment.

|image:
certif\_upload.png|

Figure 4:

Challenge view page

To update the certificate, the user can browse it by clicking
“\ **Select file**\ ” or just drag the .pem file into the upload box.

Challenge creation (Initiator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the Initiator can choose “\ **My Challenges**\ ” in
the menu bar and then click “\ **Create a new Challenge**\ ” (in the
bottom of the list of challenges).

|image:
create\_challenge.png|

Figure 5:

My challenges page

From the challenge creation page, fill the form with all information
needed for the challenge and click “\ **Create**\ ” to save it. The new
challenge will be added in the list of “my challenges”.

The following “shortcuts icons” are also available (blue: accessible,
grey: not accessible) :

|image:
modify-icon.png|
Modify the challenge (Initiator / Administrator)

|image:
delete.png|
Delete the challenge (Initiator / Administrator)

|image:
users.png|
Manage the users (Administrator)

|image:
metrics.png|
Access the evaluation of applications (Evaluator / Administrator)

Challenge modification (Initiator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the Initiator can choose “\ **My Challenges**\ ” in
the menu bar and then click on the “modify” icon |image:
modify-icon.png|
of the challenge.

Note that the challenge modification page can also be accessed from the
challenge view page (see Figure `9 <#fig_Challenge_view_page>`__).

|image:
challenge\_modify.png|

Figure 6:

Challenge modification page

Once all edit have been done, the Initiator may save the challenge by
clicking on “\ **Save Challenge**\ ”.

All fields containing information about the challenge can be edited.

Challenge promotion (join a challenge)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the top menu bar, the user can click on “Join a Challenge” and then
select a challenge by clicking on the challenge name.

Then the user access to a description of the challenge with the ability to
join the challenge.

|image:
challenge\_join.png|

Figure 7:

Challenge join page

Challenge view
^^^^^^^^^^^^^^^^^^^

The challenge view contains all the different pages associated to a
challenge. The accessible pages are not the same depending on the role of
the challenge.

The pages are accessible from a vertical menu bar on the left.

|image:
challengeview\_menu.png|

Figure 8:

Challenge view menu bar

The list of pages accessible are (with type of user who can access it):

-  |image:
   challengeview\_menu\_home.png|
   Challenge description (all)
-  |image:
   challengeview\_menu\_datapackage.png|
   Data packages (all)
-  |image:
   challengeview\_menu\_users.png|
   Challenge users (initiator / administrator)
-  |image:
   challengeview\_menu\_environments.png|
   Environments (all)
-  |image:
   challengeview\_menu\_criteria.png|
   Criteria importance/weights (participant / evaluator / administrator)
-  |image:
   challengeview\_menu\_applications.png|
   Participants applications (participant / evaluator / administrator)
-  |image:
   challengeview\_menu\_metrics.png|
   Evaluation metrics (evaluator / administrator)
-  |image:
   challengeview\_menu\_evaluationresults.png|
   Evaluation results (participants / evaluator / administrator)
-  |image:
   challengeview\_menu\_ranking.png|
   Ranking (all)

Challenge view (global description)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the user can choose “\ **My Challenges**\ ” in the
menu bar and then click on the challenge name to select it.

The first page he will see is the challenge description page.

|image:
challengeview\_description.png|

Figure 9:

Challenge view page

The Initiator has the possiblity from this page to **Modify** or
**Delete** the challenge. He can also do the following actions, clicking
on the corresponding button (right of the status):

-  **Make the challenge visible**\ (challenge is visible but not open for
   participants to join)
-  **Open challenge** (challenge is visible and participants can join)
-  **Start challenge**\ (challenge starts)
-  **Stop challenge** (challenge stop for participants, evaluation begins)
-  **Publish challenge** (evaluation is done, the challenge is closed and
   results are available).

Challenge view - Data packages (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list of Data packages accessible for the participant is displayed,
including the items associated to this data package and the search link
used inside the application.xml file of the user application.

|image:
33\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ncludes\_challengeview\_datapackage\_participant.png|

Figure 10:

Challenge data package page (participants)

Challenge view - Data packages (Initiator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list of existing Data Package is displayed, including the items
associated to this data package and the search link used inside the
application.xml file of the user application.

It is possible to insert a new data package (fill “name”, “identifier”
and choose if it should be accessible for Participants, then click on
“\ **Insert**\ ”), edit |image:
modify-icon.png|
(change name or identifier), or delete |image:
delete\_env.png|
an existing one.

It is also possible to manage data packages items (click on “\ **Manage
Items**\ ”), cf TODO.

|image:
challengeview\_datapackage\_initiator.png|

Figure 11:

Challenge data package page (initiator)

10.2.11 Challenge view - users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the initiator can access the list of users participating
to the challenge. He can also (by clicking on the corresponding user
icon):

-  Select or change the evaluator
-  Allow or deny participants to the challenge

|image:
challengeview\_users.png|

Figure 12:

Challenge view - users page (initiator)

Challenge view - environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access information about its environments
(Initiator and Administrator can see all environments of the challenge,
but Evaluator and Participants can see only their environment).

|image:
challengeview\_environments.png|

Figure 13:

Challenge view - environments page (initiator)

For each environment, it is possible to access the dashboard |image:
dashboard.png|
as well as the oozie monitor |image:
oozie.png|
.

The dashboard contains all information about the environment.

|image:
dashboard\_page.png|

Figure 14:

Environment dashboard

The oozie monitor page list all runs associated to an environment,
including information about each part of the workflow.

|image:
oozieMonitor.png|

Figure 15:

Environment oozie monitor

For each node of the workflow, the color indicates if the task failed,
succeded or is running.

To access the information about the run, you can click on “\ **Run
information**\ ” to expend the div.

Challenge view - applications (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view (see `9 <#fig_Challenge_view_page>`__), the
application part contains the information about the application of the
participant.

|image:
42\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_challengeview\_applications\_participant.png|

Figure 16:

Application view (participant)

First the Participant has to choose an Application Reference by clicking
on |image:
appref.png|
(this correspond to the application the Participant has packaged and he
wants to use for evaluation).

|image:
update\_appref.png|

Figure 17:

Choose between application references

The Participant can set the application as ready for validation by
clicking on “\ **Application ready for validation**\ ”.

The Participant can decide later to makes change on the application and
discard the validation process by clicking to “\ **Makes changes on the
application**\ ”.

|image:
45\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ludes\_challengeview\_applications\_participant2.png|

Figure 18:

Application view (participant) - 2

Challenge view - applications (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view (see `9 <#fig_Challenge_view_page>`__), the
application part contains the information about the applications the
administrator needs to validate.

|image:
challengeview\_applications\_admin.png|

Figure 19:

Application view (admin)

The Administrator can then decide to “\ **Validate the application**\ ”
or “\ **Discard the application**\ ” if he juges its not suitable for
being evaluated, by clicking on the corresponding button.

Challenge view - applications (Evaluator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view (see `9 <#fig_Challenge_view_page>`__), the
application part contains the information about the applications the
evaluator needs to evaluate.

First the Evaluator has to choose an Application Reference by clicking
on |image:
appevalref.png|
(this correspond to the run the evaluator launched to evaluate the
application of the participant).

|image:
update\_evalref.png|

Figure 20:

Choose between evaluation references

The evaluator can “\ **Quantify”** the application (this will
automatically apply the quantification process on the application) or
set the application as “\ **Manually Evaluated”** (this means he
manually edited the quantification scores from the portal or from the
Evaluation environment) by clicking on the corresponding button.

|image:
challengeview\_applications\_evaluator.png|

Figure 21:

Application view (evaluator)

The Evaluator can also apply quantification on all applications
(“\ **Quantify all”**) or set them all as manually quantified
(“\ **Quantify all (manually)”**).

Once all applications are quantified, the evaluator can do the final
step of the evaluation which is the normalization by clicking on
“\ **Evaluate all**\ ”. This will normalize all applications together
and create scores between 0 and 1 for each criterion. It will also apply
selected weights on each criterion (see
`22 <#fig_Challenge_evalTree_modification_page>`__).

Challenge view - criteria importance/weights (Evaluator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the challenge view, evaluation tree can be updated in the following
way:

-  change weight of a specific criterion (selection with radio button),
-  add new criterion to the challenge, clicking “\ **Include**\ ” (the
   criterion has to be created by the administrator, see `Section
   10.2.27 <#sub_Manage_Evaluation_Tree>`__),
-  remove existing criterion from the challenge, clicking
   “\ **Exclude**\ ” (the criterion is only removed from the challenge,
   not at the global level).

|image:
50\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_challengeview\_evaluationtree\_evaluator.png|

Figure 22:

Challenge Evaluation Tree modification page

Challenge view - criteria importance/weights (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this view, the user can see weights that have been associated to
criteria used in the challenge.

|image:
51\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_udes\_challengeview\_evaluationtree\_participant.png|

Figure 23:

Challenge Evaluation Tree view page

Challenge view - metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the Evaluator can trigger evaluation results, such as
metrics and quantification scores.

Metrics are results from the run of the participant's application.
Evaluator can add new metrics which will be used for the evaluation
process.

|image:
challengeview\_metrics.png|

Figure 24:

Challenge Evaluation Metrics view page

Quantification scores are results from the quantification of the
participant's application, taking metrics as an input. Scripts are also
available on the Evaluation platform to do all these actions in a
easiest way (cf TODO).

|image:
challengeview\_scores.png|

Figure 25:

Challenge Evaluation Quantification scores view page

Linguistic Terms are key/value association made from the Evaluator to
evaluate some criterion whose value is a string.

|image:
challengeview\_linguisticterms.png|

Figure 26:

Challenge Evaluation Quantification scores view page

Challenge view - evaluation results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the results of the evaluation of the
challenge. He can have in a quick look the view of all partcipant's scores
amongst each other, and access more detailed results.

Moving the mouse over one participant's name will make it appear in bold
compare to the others in the graph. Clicking on |image:
challengeview\_menu\_evaluationresults.png|
on the table will redirect to the specified evaluation of the
corresponding participant (see `Section
<#sub_Participant_evaluation_view>`__).

|image:
challengeview\_evaluationresults.png|

Figure 27:

Challenge Evaluation results view page

Challenge view - ranking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the ranking of the challenge (note
this page is also visible without being logged, but some information may
be not visible in that case).

|image:
challengeview\_ranking.png|

Figure 28:

Challenge ranking page

Data package items management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the Initiator can select the items he wants to have in
the data package. He would need first to select the data series he wants
to use to find items bu clicking on “\ **Select another Series”**.

There are several ways to add items on the data package:

-  Add any link manually, by clicking “\ **Manually Add new Location”**
-  Add an Opensearch url, by cliking “\ **Add Opensearch url”** once the
   search request build
-  Add one or several items from the results on the map, choosing
   “\ **Selection Mode”** on the map (click on one or several item to
   select them)

Once data package items added, click on “\ **Save”**.

To build the Opensearch request, click on |image:
search.png|
and fill the parameters that correspond to the search. It is possible to
click on |image:
bbox2.png|
or |image:
bbox1.png|
to respectively draw a rectangle or a polygon on a map that will
correspond to the search area (geo:box).

|image:
datapackage\_item\_management.png|

Figure 29:

Data package items management page

Participant evaluation view
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each participant can access its own evaluation results. It correspond to
a page showing a graph with for each criterion the min and max score as
well as Participant score.

It is also possible to switch between normalized scores and raw scores
(not normalized) of the participant.

The user can also dowload a csv file containing all the results by
clicking on |image:
evaluation.png|

Figure 30:

Participant evaluation visualization

Access Control Panel (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Control Panel is accessible only for the Administrator. It can be
accessed by clicking on “Settings” |image:
settings.png|
from the menu bar.

|image:
controlpanel.png|

Figure 31:

Control panel

Manage Users (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage User**\ s”.

To manage users for a challenge, if not selected, select the tab
“\ **Users by Challenges**\ ”.

|image:
user\_management.png|

Figure 32:

User management page

Click on “change” to change either the Initiator or the Evaluator of the
challenge, and then select the user you want to choose.

Click on “manage” to accept or reject participants for a challenge. From
there, you can Accept |image:
accept.png|
or Deny |image:
denied.png|
a user.

|image:
participant\_management.png|

Figure 33:

Challenge participants management page

To manage users in general, if not selected, select the tab “\ **All
Users**\ ”.

From there it is possible to set a user as global Initiator (this user
will have rights to create a new challenge).

|image:
user\_management3.png|

Figure 34:

Challenge participants management page

Manage Data Series (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage Series**\ ”. The list of
existing series will appear. To create a new one click on “\ **Add Data
Series**\ ”.

Once all the fields filled, save by clicking “\ **Insert**\ ”.

|image:
series\_creation.png|

Figure 35:

Page to apply to a challenge

Manage Environments (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage** **Environments**\ ”.

|image:
manage\_environment.png|

Figure 36:

Challenge environment management page

The Template Settings part allow to select the provider, virtual network
and template for the challenge. These settings will be used when the
environments are generated.

To create a new environment, click on “\ **Create**\ ”.

It is also possible to stop |image:
stop\_env.png|
, resume |image:
start\_env.png|
or delete |image:
delete\_env.png|
an existing environment.

See also `14 <#fig_Environment_dashboard>`__ and
`15 <#fig_Environment_ooziemonitor>`__.

Manage Criteria (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage** **Criteria”**.

The Administrator can manage the criteria (independently of challenges)
from this page by creating new ones |image:
new\_criterion.png|
or deleting definitively existing ones |image:
new\_criterion\_Description.png|

Figure 37:

Evaluation Tree management page (adding a new criterion)

The “Unit/Dimension” field is a list representing the unit of the value
of the criterion.

The “Quantification” and “Normalization” fields are both meant to
contain formulas. To write a formula, add “$$” in the beginning and in
the end of the latex formula. The formula will be displayed on the right
part.

The “Quantification\_logic” is the logic used for normalization of the
value obtained after quantification. It can be chosen between “Higher is
Better” and “Lower is Better”.

The “Actor” field indicates who is calculating the value of the
criterion. It could be the system or the evaluator.

Save the new criterion by clickin on “\ **Save Criterion**\ ”.

Clicking on “\ **Show info / Modify Criteria**\ ” will open the Criteria
view.

|image:
criterion\_page.png|

Figure 38:

Criterion view

Support (All users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The support page is accessible from the menu bar, by clicking on
“\ **Support**\ ”. It gives the possibility to a user to have access to
the list of existing support tickets or to create a new one (by clicking
on “\ **New issue**\ ”). Clicking on the Title of the ticket will
redirect to the redmine support page.

|image:
html\_support.png|

Figure 39:

List of support tickets

During the creation of a new ticket, from the interface you can set the
Subject, the Priority as well as the Description. The Assignee will be
by default the E-CEO support team. The ticket can be updated with more
details directly on the redmine support page.

|image:
html\_support2.png|

Figure 40:

Creation of support tickets

Notifications (All users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notifications can be accessed by clicking |image:
bell.png|
in the top of any page. The following list will appear, with all
notifications associated to the current user, along with the number of
days ago it was created. Notifications are ordered by date, from the
newest to the oldest.

|image:
notifications.png|

Figure 41:

Notifications list

Clicking on a notification will redirect the browser to the page
corresponding to the notification. The clicked notification will be
removed from the list and considered as “read”.

Notifications can also be accessed by clicking to the link |image:
rssfeed.png|
. The linked page contains a rss feed with all notifications (and could
be used by any feed reader.

|image:
notifications\_feed.png|

Figure 42:

Notifications rss feed

Error messages
~~~~~~~~~~~~~~~~~~~

When an error occurs, a pop-up message will appear explaining what is
the error to the user.

Evaluation tools
~~~~~~~~~~~~~~~~~~~~~

On the Evaluation environment, a list of tools is available to ease
Evaluator's evaluation process.

eceo-addmetrics
^^^^^^^^^^^^^^^

Add a name/value element(s) into monitor/monitor.xml file of the
specified run.

usage:

-  eceo-addmetrics -r <runId> -n <metricsName> -v <metricsValue>
-  eceo-addmetrics -r <runId> -f <metricsFile>

|image:
metricsxml.png|

Figure 43:

Input Metrics file example

eceo-addscore
^^^^^^^^^^^^^

Add a name/value element into monitor/scores.xml file of the specified
run. Score is the result of quantification process.

usage:

-  eceo-addscore-r <runId> -n <scoreName> -v <scoreValue>
-  eceo-addscore-r <runId> -f <scoreFile>

|image:
scoresxml.png|

Figure 44:

Input Scores file example

eceo-csvtoscore
^^^^^^^^^^^^^^^

Update the file monitor/scores.xml of the specified run using entries
inside the csv. Score is the result of quantification process.

usage:

-  eceo-csvtoscore -f <csvFile>

|image:
scorescsv.png|

Figure 45:

Input Scores csv file example (excel view)

|image:
scorecsvtext.png|

Figure 46:

Input Scores csv file example (text view)

eceo-csvtoxmlscore
^^^^^^^^^^^^^^^^^^

Create a list of scores-runID.xml files. Score is the result of
quantification process.

Evaluator can then review them and upload them into the run folder using
eceo-addscore command.

usage:

-  eceo-csvtoxmlscore -f <csvFile>

Tutorial
-----------

Participant application creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A tutorial to create a simple application for a Participant on a Private
Environment is available here:
`https://support.terradue.com/projects/sandbox-demo/wiki/Lib-beam <https://support.terradue.com/projects/sandbox-demo/wiki/Lib-beam>`__.

.. |image: challenge\_created.png| image:: challenge_created.png
.. |image: challenge\_promoted.png| image:: challenge_promoted.png
.. |image: challenge\_open.png| image:: challenge_open.png
.. |image: challenge\_in\_progress.png| image:: challenge_in_progress.png
.. |image: challenge\_on\_evaluation.png| image:: challenge_on_evaluation.png
.. |image: challenge\_closed.png| image:: challenge_closed.png
.. |image: settings.png| image:: settings.png
.. |image: homepage.png| image:: homepage.png
.. |image: user\_info.png| image:: user_info.png
.. |image: user\_profile.png| image:: user_profile.png
.. |image: certif\_upload.png| image:: certif_upload.png
.. |image: create\_challenge.png| image:: create_challenge.png
.. |image: modify-icon.png| image:: modify-icon.png
.. |image: delete.png| image:: delete.png
.. |image: users.png| image:: users.png
.. |image: metrics.png| image:: metrics.png
.. |image: challenge\_modify.png| image:: challenge_modify.png
.. |image: challenge\_join.png| image:: challenge_join.png
.. |image: challengeview\_menu.png| image:: challengeview_menu.png
.. |image: challengeview\_menu\_home.png| image:: challengeview_menu_home.png
.. |image: challengeview\_menu\_datapackage.png| image:: challengeview_menu_datapackage.png
.. |image: challengeview\_menu\_users.png| image:: challengeview_menu_users.png
.. |image: challengeview\_menu\_environments.png| image:: challengeview_menu_environments.png
.. |image: challengeview\_menu\_criteria.png| image:: challengeview_menu_criteria.png
.. |image: challengeview\_menu\_applications.png| image:: challengeview_menu_applications.png
.. |image: challengeview\_menu\_metrics.png| image:: challengeview_menu_metrics.png
.. |image: challengeview\_menu\_evaluationresults.png| image:: challengeview_menu_evaluationresults.png
.. |image: challengeview\_menu\_ranking.png| image:: challengeview_menu_ranking.png
.. |image: challengeview\_description.png| image:: challengeview_description.png
.. |image: 33\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ncludes\_challengeview\_datapackage\_participant.png| image:: 33_Users_enguerran_Terradue_workspace_ECEO_deve___ncludes_challengeview_datapackage_participant.png
.. |image: delete\_env.png| image:: delete_env.png
.. |image: challengeview\_datapackage\_initiator.png| image:: challengeview_datapackage_initiator.png
.. |image: challengeview\_users.png| image:: challengeview_users.png
.. |image: challengeview\_environments.png| image:: challengeview_environments.png
.. |image: dashboard.png| image:: dashboard.png
.. |image: oozie.png| image:: oozie.png
.. |image: dashboard\_page.png| image:: dashboard_page.png
.. |image: oozieMonitor.png| image:: oozieMonitor.png
.. |image: 42\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_challengeview\_applications\_participant.png| image:: 42_Users_enguerran_Terradue_workspace_ECEO_deve___cludes_challengeview_applications_participant.png
.. |image: appref.png| image:: appref.png
.. |image: update\_appref.png| image:: update_appref.png
.. |image: 45\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ludes\_challengeview\_applications\_participant2.png| image:: 45_Users_enguerran_Terradue_workspace_ECEO_deve___ludes_challengeview_applications_participant2.png
.. |image: challengeview\_applications\_admin.png| image:: challengeview_applications_admin.png
.. |image: appevalref.png| image:: appevalref.png
.. |image: update\_evalref.png| image:: update_evalref.png
.. |image: challengeview\_applications\_evaluator.png| image:: challengeview_applications_evaluator.png
.. |image: 50\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_challengeview\_evaluationtree\_evaluator.png| image:: 50_Users_enguerran_Terradue_workspace_ECEO_deve___cludes_challengeview_evaluationtree_evaluator.png
.. |image: 51\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_udes\_challengeview\_evaluationtree\_participant.png| image:: 51_Users_enguerran_Terradue_workspace_ECEO_deve___udes_challengeview_evaluationtree_participant.png
.. |image: challengeview\_metrics.png| image:: challengeview_metrics.png
.. |image: challengeview\_scores.png| image:: challengeview_scores.png
.. |image: challengeview\_linguisticterms.png| image:: challengeview_linguisticterms.png
.. |image: challengeview\_evaluationresults.png| image:: challengeview_evaluationresults.png
.. |image: challengeview\_ranking.png| image:: challengeview_ranking.png
.. |image: search.png| image:: search.png
.. |image: bbox2.png| image:: bbox2.png
.. |image: bbox1.png| image:: bbox1.png
.. |image: datapackage\_item\_management.png| image:: datapackage_item_management.png
.. |image: csv\_download.png| image:: csv_download.png
.. |image: evaluation.png| image:: evaluation.png
.. |image: controlpanel.png| image:: controlpanel.png
.. |image: user\_management.png| image:: user_management.png
.. |image: accept.png| image:: accept.png
.. |image: denied.png| image:: denied.png
.. |image: participant\_management.png| image:: participant_management.png
.. |image: user\_management3.png| image:: user_management3.png
.. |image: series\_creation.png| image:: series_creation.png
.. |image: manage\_environment.png| image:: manage_environment.png
.. |image: stop\_env.png| image:: stop_env.png
.. |image: start\_env.png| image:: start_env.png
.. |image: new\_criterion.png| image:: new_criterion.png
.. |image: delete\_criterion.png| image:: delete_criterion.png
.. |image: new\_criterion\_Description.png| image:: new_criterion_Description.png
.. |image: criterion\_page.png| image:: criterion_page.png
.. |image: html\_support.png| image:: html_support.png
.. |image: html\_support2.png| image:: html_support2.png
.. |image: bell.png| image:: bell.png
.. |image: notifications.png| image:: notifications.png
.. |image: rssfeed.png| image:: rssfeed.png
.. |image: notifications\_feed.png| image:: notifications_feed.png
.. |image: metricsxml.png| image:: metricsxml.png
.. |image: scoresxml.png| image:: scoresxml.png
.. |image: scorescsv.png| image:: scorescsv.png
.. |image: scorecsvtext.png| image:: scorecsvtext.png
