
Participant Guide
=================

Role description
----------------

A **participant** in E-CEO platform is a contestee, participating to a challenge.

Challenge **participants** will use the platform to:

-  get information about a challenge,
-  get information about their Private Environment,
-  get support from the support team,
-  provide information about their application,
-  get application evaluation result


Join a Challenge
----------------

On the top menu bar, the user can click on **Join a Challenge** and then select a challenge by clicking on the challenge name.
Challenges to be joined can also be accessible from the home page.

Then the user access to a description of the challenge with the ability to join the challenge.

|contestjoin.png|


Challenge view
--------------

The challenge view contains all the different pages associated to a challenge. The accessible pages are not the same depending on the role of the challenge.
The pages are accessible from a vertical menu bar on the left.

The list of pages accessible for a **participant** are:

-  |contestviewmenuhome.png| Challenge description
-  |contestviewmenudatapackage.png| Data packages
-  |contestviewmenuenvironments.png| Environments
-  |contestviewmenucriteria.png| Criteria importance/weights
-  |contestviewmenuapplications.png| Participants applications
-  |contestviewmenuevaluationresults.png| Evaluation results
-  |contestviewmenuranking.png| Ranking

Global description
^^^^^^^^^^^^^^^^^^

From the home page, the user can choose **My Challenges** in the
menu bar and then click on the challenge name to select it.

The first page he will see is the challenge description page.

.. image:: includes/sum/contestview_description.png
	:align: center

The **participant** can Join a challenge from this page.

Data packages
^^^^^^^^^^^^^

The list of Data packages accessible for the participant is displayed,
including the items associated to this data package and the search link
used inside the application.xml file of the user application.

.. image:: includes/sum/contestview_datapackage_participant.png
	:align: center
	
Environments
^^^^^^^^^^^^

From this page, the user can access information about its environments (Initiator and Administrator can see all environments of the challenge, but Evaluator and Participants can see only their environment).

.. image:: includes/sum/contestview_environments.png
	:align: center

For each environment, it is possible to access the dashboard |dashboard.png|
as well as the oozie monitor |oozie.png|.

The dashboard contains all information about the environment.

.. image:: includes/sum/dashboard_page.png
	:align: center

The oozie monitor page list all runs associated to an environment,
including information about each part of the workflow.

.. image:: includes/sum/oozieMonitor.png
	:align: center
	
For each node of the workflow, the color indicates if the task failed, succeded or is running.

To access the information about the run, you can click on **Run information** to expend the div.

Participants applications
^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view, the application part contains the information about the application of the
participant.

.. image:: includes/sum/contestview_applications_participant.png
	:align: center

First the Participant has to choose an Application Reference by clicking on |appref.png|
(this correspond to the application the Participant has packaged and he wants to use for evaluation).

.. image:: includes/sum/update_appref.png
	:align: center
	
The Participant can set the application as ready for validation by
clicking on **Application ready for validation**.

The Participant can decide later to makes change on the application and
discard the validation process by clicking to **Makes changes on the application**.

.. image:: includes/sum/contestview_applications_participant2.png
	:align: center

Criteria importance/weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this view, the user can see weights that have been associated to criteria used in the challenge.

.. image:: includes/sum/contestview_evaluationtree_participant.png
	:align: center

Evaluation results
^^^^^^^^^^^^^^^^^^

From this page, the user can access the results of the evaluation of the
challenge. He can have in a quick look the view of all partcipant's scores
amongst each other, and access more detailed results.

Moving the mouse over one participant's name will make it appear in bold
compare to the others in the graph. Clicking on |contestviewmenuevaluationresults.png|
on the table will redirect to the specified evaluation of the corresponding participant.

.. image:: includes/sum/contestview_evaluationresults.png
	:align: center

Participant evaluation view
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each participant can access its own evaluation results. It correspond to
a page showing a graph with for each criterion the min and max score as
well as Participant score.

It is also possible to switch between normalized scores and raw scores
(not normalized) of the participant.

The user can also dowload a csv file containing all the results by
clicking on |evaluation.png|

Ranking
^^^^^^^

From this page, the user can access the ranking of the challenge (note
this page is also visible without being logged, but some information may
be not visible in that case).

.. image:: includes/sum/contestview_ranking.png
	:align: center


Tutorial
--------

Participant application creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A tutorial to create a simple application for a Participant on a Private
Environment is available here: `https://support.terradue.com/projects/sandbox-demo/wiki/Lib-beam <https://support.terradue.com/projects/sandbox-demo/wiki/Lib-beam>`__.

.. |contestviewmenuhome.png| image:: includes/sum/contestview_menu_home.png
.. |contestviewmenudatapackage.png| image:: includes/sum/contestview_menu_datapackage.png
.. |contestviewmenuenvironments.png| image:: includes/sum/contestview_menu_environments.png
.. |contestviewmenucriteria.png| image:: includes/sum/contestview_menu_criteria.png
.. |contestviewmenuapplications.png| image:: includes/sum/contestview_menu_applications.png
.. |contestviewmenuevaluationresults.png| image:: includes/sum/contestview_menu_evaluationresults.png
.. |contestviewmenuranking.png| image:: includes/sum/contestview_menu_ranking.png
.. |dashboard.png| image:: includes/sum/dashboard.png
.. |oozie.png| image:: includes/sum/oozie.png
.. |appref.png| image:: includes/sum/appref.png
.. |evaluation.png| image:: includes/sum/evaluation.png
.. |contestjoin.png| image:: includes/sum/contest_join.png

