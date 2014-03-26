

Purpose of the software
-------------------------

The project addresses the technologies and architectures needed to
provide a collaborative research Platform for automating data mining and
information extraction experiments. The Platform serves for the
implementation of open contests focusing on Information Extraction for
EO applications. The possibility to implement – through the contests –
different approaches and algorithms in a common Software Environment
(provided by the collaborative Platform) facilitates the comparison and
the evaluation between different methodologies, which is one of the main
requirements requested by scientific experts who develop algorithms in
the EO field. The project objectives are to provide a collaborative
research Platform for:

- Automation of data mining and information extraction experiments

- Generation of reproducible results that can be easily shared

- Addressing specific scientific challenges and tackling new research problems in a “parallel and collaborative way”

The platform allows the set-up three on-line contests, which can be
appealing way of conducting research in data mining.

The platform is composed of a front-end (GUI) and a back-end
(webserver).

The software can be use by 4 type of users: Participants, Initiators,
Evaluators, Administrators.

Contest **participants** will use the platform to:

-  get information about a contest,
-  get information about their Private Environment,
-  get support from the support team,
-  provide information about their application,
-  get application evaluation result

Contest **initiators** will use the platform to:

-  define a contest,
-  get contest status and evolution,
-  accept or reject users for a contest,
-  define data packages

Contest **evaluators** will use the platform to:

-  define contest evaluation tree,
-  evaluate participant application,
-  get information about the Evaluation Environment

Contest **administrators** will use the platform to:

-  accept or reject users for a contest,
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

Contest creation and definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Creation of the contest and definition of the basic informations.

Contest modification
~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Modification of the contest information.

Contest promotion
~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Validates the contest definition and makes it available for application
by Participants.

Application to a contest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Participant**

Apply to participate to a contest.

Contest start
~~~~~~~~~~~~~~~~~

**Portal Agent**

Update the status of the contest. Make available all packages on the
environments.

Contest stop
~~~~~~~~~~~~~~~~

**Portal Agent**

Update the status of the contest. Participant cannot package new
Application.

Contest users management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add new Initiator / Change contest Initiator or Evaluator / Accept or
deny Participant for a contest.

Series management
~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Add new series in the database.

Data package management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Create new data packages from the series.

Data package for contest management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Initiator**

Associate data package to a contest.

Contest Environment management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Administrator**

Choose template, provider and virtual network for a contest. Create
environments

Environment creation
~~~~~~~~~~~~~~~~~~~~~~~~~

**Portal Agent / Administrator**

Automatic environment creation X days before the start of the contest by
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
available for all contests).

Evaluation Tree management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Evaluator**

Associate a criterion to a contest or remove a criterion from a contest.

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

A contest (which is the core part of the portal) is divided into 6
phases:

#. Contest is under creation |image:
   contest\_created.png|
#. Contest is visible |image:
   contest\_promoted.png|
#. Contest is open to applications |image:
   contest\_open.png|
#. Contest is In Progress |image:
   contest\_in\_progress.png|
#. Contest is On Evaluation |image:
   contest\_on\_evaluation.png|
#. Contest is Closed |image:
   contest\_closed.png|

Normal operations
~~~~~~~~~~~~~~~~~~~~~

See `Section 8 <#sec_Operations_basics>`__ for details about all listed
operations.

Phase 1 (Contest created)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Contest creation and definition
-  Contest modification
-  Contest promotion
-  Contest users management (initiator/evaluator)
-  Series and data package management
-  Data package for contest management
-  Contest Environment management
-  Evaluation Criterion creation
-  Evaluation Tree management
-  Notifications cleaning

Phase 2 (Contest visible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Contest description can be accessed

Phase 3 (Contest promoted)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Application to a contest
-  User certificate upload
-  Contest start
-  Contest users management (participants)
-  Environment creation
-  Notifications cleaning

Phase 4 (Contest started)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Participant Application status update (packaging)
-  Participant Application status update (validation)
-  Participant Application references update
-  Contest stop
-  Notifications cleaning

Phase 5 (Contest ended / on evaluation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Participant Application status update (evaluation)
-  Participant Application references update
-  Environment nodes scalability
-  Notifications cleaning

Phase 6 (Contest closed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Contest results are published and accessible.

Reference manual
-------------------

Introduction
~~~~~~~~~~~~~~~~~

Screen definitions and operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Home page

The home page of the E-CEO portal is as shown in the following figure.
It contains a top bar, which is an quick access to all type of contest
of the portal:

-  My Contests: the contests I am involved in.
-  Join a Contest: open or on-going contests that a user can join.
-  Upcoming Contests: future contests that a user cannot yet join.
-  Past Contests: closed contests, only results are accessible.
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

Contest view page

To update the certificate, the user can browse it by clicking
“\ **Select file**\ ” or just drag the .pem file into the upload box.

Contest creation (Initiator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the Initiator can choose “\ **My Contests**\ ” in
the menu bar and then click “\ **Create a new Contest**\ ” (in the
bottom of the list of contests).

|image:
create\_contest.png|

Figure 5:

My contests page

From the contest creation page, fill the form with all information
needed for the contest and click “\ **Create**\ ” to save it. The new
contest will be added in the list of “my contests”.

The following “shortcuts icons” are also available (blue: accessible,
grey: not accessible) :

|image:
modify-icon.png|
Modify the contest (Initiator / Administrator)

|image:
delete.png|
Delete the contest (Initiator / Administrator)

|image:
users.png|
Manage the users (Administrator)

|image:
metrics.png|
Access the evaluation of applications (Evaluator / Administrator)

Contest modification (Initiator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the Initiator can choose “\ **My Contests**\ ” in
the menu bar and then click on the “modify” icon |image:
modify-icon.png|
of the contest.

Note that the contest modification page can also be accessed from the
contest view page (see Figure `9 <#fig_Contest_view_page>`__).

|image:
contest\_modify.png|

Figure 6:

Contest modification page

Once all edit have been done, the Initiator may save the contest by
clicking on “\ **Save Contest**\ ”.

All fields containing information about the contest can be edited.

Contest promotion (join a contest)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the top menu bar, the user can click on “Join a Contest” and then
select a contest by clicking on the contest name.

Then the user access to a description of the contest with the ability to
join the contest.

|image:
contest\_join.png|

Figure 7:

Contest join page

Contest view
^^^^^^^^^^^^^^^^^^^

The contest view contains all the different pages associated to a
contest. The accessible pages are not the same depending on the role of
the contest.

The pages are accessible from a vertical menu bar on the left.

|image:
contestview\_menu.png|

Figure 8:

Contest view menu bar

The list of pages accessible are (with type of user who can access it):

-  |image:
   contestview\_menu\_home.png|
   Contest description (all)
-  |image:
   contestview\_menu\_datapackage.png|
   Data packages (all)
-  |image:
   contestview\_menu\_users.png|
   Contest users (initiator / administrator)
-  |image:
   contestview\_menu\_environments.png|
   Environments (all)
-  |image:
   contestview\_menu\_criteria.png|
   Criteria importance/weights (participant / evaluator / administrator)
-  |image:
   contestview\_menu\_applications.png|
   Participants applications (participant / evaluator / administrator)
-  |image:
   contestview\_menu\_metrics.png|
   Evaluation metrics (evaluator / administrator)
-  |image:
   contestview\_menu\_evaluationresults.png|
   Evaluation results (participants / evaluator / administrator)
-  |image:
   contestview\_menu\_ranking.png|
   Ranking (all)

Contest view (global description)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the user can choose “\ **My Contests**\ ” in the
menu bar and then click on the contest name to select it.

The first page he will see is the contest description page.

|image:
contestview\_description.png|

Figure 9:

Contest view page

The Initiator has the possiblity from this page to **Modify** or
**Delete** the contest. He can also do the following actions, clicking
on the corresponding button (right of the status):

-  **Make the contest visible**\ (contest is visible but not open for
   participants to join)
-  **Open contest** (contest is visible and participants can join)
-  **Start contest**\ (contest starts)
-  **Stop contest** (contest stop for participants, evaluation begins)
-  **Publish contest** (evaluation is done, the contest is closed and
   results are available).

Contest view - Data packages (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list of Data packages accessible for the participant is displayed,
including the items associated to this data package and the search link
used inside the application.xml file of the user application.

|image:
33\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ncludes\_contestview\_datapackage\_participant.png|

Figure 10:

Contest data package page (participants)

Contest view - Data packages (Initiator)
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
contestview\_datapackage\_initiator.png|

Figure 11:

Contest data package page (initiator)

10.2.11 Contest view - users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the initiator can access the list of users participating
to the contest. He can also (by clicking on the corresponding user
icon):

-  Select or change the evaluator
-  Allow or deny participants to the contest

|image:
contestview\_users.png|

Figure 12:

Contest view - users page (initiator)

Contest view - environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access information about its environments
(Initiator and Administrator can see all environments of the contest,
but Evaluator and Participants can see only their environment).

|image:
contestview\_environments.png|

Figure 13:

Contest view - environments page (initiator)

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

Contest view - applications (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the contest view (see `9 <#fig_Contest_view_page>`__), the
application part contains the information about the application of the
participant.

|image:
42\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_contestview\_applications\_participant.png|

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
45\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ludes\_contestview\_applications\_participant2.png|

Figure 18:

Application view (participant) - 2

Contest view - applications (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the contest view (see `9 <#fig_Contest_view_page>`__), the
application part contains the information about the applications the
administrator needs to validate.

|image:
contestview\_applications\_admin.png|

Figure 19:

Application view (admin)

The Administrator can then decide to “\ **Validate the application**\ ”
or “\ **Discard the application**\ ” if he juges its not suitable for
being evaluated, by clicking on the corresponding button.

Contest view - applications (Evaluator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the contest view (see `9 <#fig_Contest_view_page>`__), the
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
contestview\_applications\_evaluator.png|

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
`22 <#fig_Contest_evalTree_modification_page>`__).

Contest view - criteria importance/weights (Evaluator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the contest view, evaluation tree can be updated in the following
way:

-  change weight of a specific criterion (selection with radio button),
-  add new criterion to the contest, clicking “\ **Include**\ ” (the
   criterion has to be created by the administrator, see `Section
   10.2.27 <#sub_Manage_Evaluation_Tree>`__),
-  remove existing criterion from the contest, clicking
   “\ **Exclude**\ ” (the criterion is only removed from the contest,
   not at the global level).

|image:
50\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_contestview\_evaluationtree\_evaluator.png|

Figure 22:

Contest Evaluation Tree modification page

Contest view - criteria importance/weights (Participant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this view, the user can see weights that have been associated to
criteria used in the contest.

|image:
51\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_udes\_contestview\_evaluationtree\_participant.png|

Figure 23:

Contest Evaluation Tree view page

Contest view - metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the Evaluator can trigger evaluation results, such as
metrics and quantification scores.

Metrics are results from the run of the participant's application.
Evaluator can add new metrics which will be used for the evaluation
process.

|image:
contestview\_metrics.png|

Figure 24:

Contest Evaluation Metrics view page

Quantification scores are results from the quantification of the
participant's application, taking metrics as an input. Scripts are also
available on the Evaluation platform to do all these actions in a
easiest way (cf TODO).

|image:
contestview\_scores.png|

Figure 25:

Contest Evaluation Quantification scores view page

Linguistic Terms are key/value association made from the Evaluator to
evaluate some criterion whose value is a string.

|image:
contestview\_linguisticterms.png|

Figure 26:

Contest Evaluation Quantification scores view page

Contest view - evaluation results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the results of the evaluation of the
contest. He can have in a quick look the view of all partcipant's scores
amongst each other, and access more detailed results.

Moving the mouse over one participant's name will make it appear in bold
compare to the others in the graph. Clicking on |image:
contestview\_menu\_evaluationresults.png|
on the table will redirect to the specified evaluation of the
corresponding participant (see `Section
<#sub_Participant_evaluation_view>`__).

|image:
contestview\_evaluationresults.png|

Figure 27:

Contest Evaluation results view page

Contest view - ranking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the ranking of the contest (note
this page is also visible without being logged, but some information may
be not visible in that case).

|image:
contestview\_ranking.png|

Figure 28:

Contest ranking page

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

To manage users for a contest, if not selected, select the tab
“\ **Users by Contests**\ ”.

|image:
user\_management.png|

Figure 32:

User management page

Click on “change” to change either the Initiator or the Evaluator of the
contest, and then select the user you want to choose.

Click on “manage” to accept or reject participants for a contest. From
there, you can Accept |image:
accept.png|
or Deny |image:
denied.png|
a user.

|image:
participant\_management.png|

Figure 33:

Contest participants management page

To manage users in general, if not selected, select the tab “\ **All
Users**\ ”.

From there it is possible to set a user as global Initiator (this user
will have rights to create a new contest).

|image:
user\_management3.png|

Figure 34:

Contest participants management page

Manage Data Series (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage Series**\ ”. The list of
existing series will appear. To create a new one click on “\ **Add Data
Series**\ ”.

Once all the fields filled, save by clicking “\ **Insert**\ ”.

|image:
series\_creation.png|

Figure 35:

Page to apply to a contest

Manage Environments (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select “\ **Manage** **Environments**\ ”.

|image:
manage\_environment.png|

Figure 36:

Contest environment management page

The Template Settings part allow to select the provider, virtual network
and template for the contest. These settings will be used when the
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

The Administrator can manage the criteria (independently of contests)
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

.. |image: contest\_created.png| image:: contest_created.png
.. |image: contest\_promoted.png| image:: contest_promoted.png
.. |image: contest\_open.png| image:: contest_open.png
.. |image: contest\_in\_progress.png| image:: contest_in_progress.png
.. |image: contest\_on\_evaluation.png| image:: contest_on_evaluation.png
.. |image: contest\_closed.png| image:: contest_closed.png
.. |image: settings.png| image:: settings.png
.. |image: homepage.png| image:: homepage.png
.. |image: user\_info.png| image:: user_info.png
.. |image: user\_profile.png| image:: user_profile.png
.. |image: certif\_upload.png| image:: certif_upload.png
.. |image: create\_contest.png| image:: create_contest.png
.. |image: modify-icon.png| image:: modify-icon.png
.. |image: delete.png| image:: delete.png
.. |image: users.png| image:: users.png
.. |image: metrics.png| image:: metrics.png
.. |image: contest\_modify.png| image:: contest_modify.png
.. |image: contest\_join.png| image:: contest_join.png
.. |image: contestview\_menu.png| image:: contestview_menu.png
.. |image: contestview\_menu\_home.png| image:: contestview_menu_home.png
.. |image: contestview\_menu\_datapackage.png| image:: contestview_menu_datapackage.png
.. |image: contestview\_menu\_users.png| image:: contestview_menu_users.png
.. |image: contestview\_menu\_environments.png| image:: contestview_menu_environments.png
.. |image: contestview\_menu\_criteria.png| image:: contestview_menu_criteria.png
.. |image: contestview\_menu\_applications.png| image:: contestview_menu_applications.png
.. |image: contestview\_menu\_metrics.png| image:: contestview_menu_metrics.png
.. |image: contestview\_menu\_evaluationresults.png| image:: contestview_menu_evaluationresults.png
.. |image: contestview\_menu\_ranking.png| image:: contestview_menu_ranking.png
.. |image: contestview\_description.png| image:: contestview_description.png
.. |image: 33\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ncludes\_contestview\_datapackage\_participant.png| image:: 33_Users_enguerran_Terradue_workspace_ECEO_deve___ncludes_contestview_datapackage_participant.png
.. |image: delete\_env.png| image:: delete_env.png
.. |image: contestview\_datapackage\_initiator.png| image:: contestview_datapackage_initiator.png
.. |image: contestview\_users.png| image:: contestview_users.png
.. |image: contestview\_environments.png| image:: contestview_environments.png
.. |image: dashboard.png| image:: dashboard.png
.. |image: oozie.png| image:: oozie.png
.. |image: dashboard\_page.png| image:: dashboard_page.png
.. |image: oozieMonitor.png| image:: oozieMonitor.png
.. |image: 42\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_contestview\_applications\_participant.png| image:: 42_Users_enguerran_Terradue_workspace_ECEO_deve___cludes_contestview_applications_participant.png
.. |image: appref.png| image:: appref.png
.. |image: update\_appref.png| image:: update_appref.png
.. |image: 45\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_ludes\_contestview\_applications\_participant2.png| image:: 45_Users_enguerran_Terradue_workspace_ECEO_deve___ludes_contestview_applications_participant2.png
.. |image: contestview\_applications\_admin.png| image:: contestview_applications_admin.png
.. |image: appevalref.png| image:: appevalref.png
.. |image: update\_evalref.png| image:: update_evalref.png
.. |image: contestview\_applications\_evaluator.png| image:: contestview_applications_evaluator.png
.. |image: 50\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_cludes\_contestview\_evaluationtree\_evaluator.png| image:: 50_Users_enguerran_Terradue_workspace_ECEO_deve___cludes_contestview_evaluationtree_evaluator.png
.. |image: 51\_Users\_enguerran\_Terradue\_workspace\_ECEO\_deve\_\_\_udes\_contestview\_evaluationtree\_participant.png| image:: 51_Users_enguerran_Terradue_workspace_ECEO_deve___udes_contestview_evaluationtree_participant.png
.. |image: contestview\_metrics.png| image:: contestview_metrics.png
.. |image: contestview\_scores.png| image:: contestview_scores.png
.. |image: contestview\_linguisticterms.png| image:: contestview_linguisticterms.png
.. |image: contestview\_evaluationresults.png| image:: contestview_evaluationresults.png
.. |image: contestview\_ranking.png| image:: contestview_ranking.png
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
