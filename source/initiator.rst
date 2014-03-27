
Initiator Guide
================

Role description
----------------

An **initiator** in E-CEO platform is the person in charge of a challenge. He is the one creating it and managing it during the life of the challenge.
Challenge **initiators** will use the platform to:

-  define a challenge,
-  get challenge status and evolution,
-  accept or reject users for a challenge,
-  define data packages


Challenge creation 
------------------

From the top menu bar, the **Initiator** can click on the “Settings” |settings.png| button and then click on **Create a Challenge** .
Otherwise, from the **My Challenges**  list in the menu bar, the **Initiator** can click on **Create a new Challenge**  (in the bottom of the list of challenges).

|createchallenge.png|

From the challenge creation page, fill the form with all information
needed for the challenge and click **Create**  to save it. The new
challenge will be added in the list of “my challenges”.

Challenge modification 
----------------------

From the home page, the Initiator can choose **My Challenges**  in
the menu bar and then click on the “modify” icon |modify-icon.png| of the challenge.
Note that the challenge modification page can also be accessed from the challenge view page (description view, in the bottom of the page).

|challengemodify.png|

Once all edit have been done, the Initiator may save the challenge by clicking on **Save Challenge** .
All fields containing information about the challenge can be edited.

Challenge view
--------------

The challenge view contains all the different pages associated to a
challenge. The accessible pages are not the same depending on the role of
the challenge.

The pages are accessible from a vertical menu bar on the left.

|contestviewmenu.png|

The list of pages accessible are (with type of user who can access it):

-  |contestviewmenuhome.png| Challenge description
-  |contestviewmenudatapackage.png| Data packages
-  |contestviewmenuusers.png| Challenge users
-  |contestviewmenuenvironments.png| Environments
-  |contestviewmenuevaluationresults.png| Evaluation results
-  |contestviewmenuranking.png| Ranking


Challenge view (global description)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the home page, the user can choose **My Challenges**  in the
menu bar and then click on the challenge name to select it.

The first page he will see is the challenge description page.

|contestviewdescription.png|

The Initiator has the possiblity from this page to **Modify** or
**Delete** the challenge. He can also do the following actions, clicking
on the corresponding button (right of the status):

-  **Make the challenge visible**\ (challenge is visible but not open for participants to join)
-  **Open challenge** (challenge is visible and participants can join)
-  **Start challenge**\ (challenge starts)
-  **Stop challenge** (challenge stop for participants, evaluation begins)
-  **Publish challenge** (evaluation is done, the challenge is closed and results are available).

Challenge view - Data packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list of existing Data Package is displayed, including the items
associated to this data package and the search link used inside the
application.xml file of the user application.

It is possible to insert a new data package (fill “name”, “identifier”
and choose if it should be accessible for Participants, then click on
**Insert** ), edit |modify-icon.png| (change name or identifier), or delete |deleteenv.png| an existing one.

It is also possible to manage data packages items (click on **Manage Items** ).

|contestviewdatapackageinitiator.png|

Data package items management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the Initiator can select the items he wants to have in
the data package. He would need first to select the data series he wants
to use to find items bu clicking on **Select another Series**.

There are several ways to add items on the data package:

-  Add any link manually, by clicking **Manually Add new Location**
-  Add an Opensearch url, by cliking **Add Opensearch url** once the search request build
-  Add one or several items from the results on the map, choosing **Selection Mode** on the map (click on one or several item to select them)

Once data package items added, click on **Save**.

To build the Opensearch request, click on |search.png| and fill the parameters that correspond to the search. It is possible to click on |bbox2.png|
or |bbox1.png| to respectively draw a rectangle or a polygon on a map that will correspond to the search area (geo:box).

|datapackageitemmanagement.png|

Challenge view - users
^^^^^^^^^^^^^^^^^^^^^^

From this page, the initiator can access the list of users participating
to the challenge. He can also (by clicking on the corresponding user icon):

-  Select or change the evaluator
-  Allow or deny participants to the challenge

|contestviewusers.png|

Challenge view - environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access information about its environments
(Initiator and Administrator can see all environments of the challenge,
but Evaluator and Participants can see only their environment).

|contestviewenvironments.png|

For each environment, it is possible to access the dashboard |dashboard.png| as well as the oozie monitor |oozie.png| .
The dashboard contains all information about the environment.

|dashboardpage.png|

The oozie monitor page list all runs associated to an environment,
including information about each part of the workflow.

|oozieMonitor.png|

For each node of the workflow, the color indicates if the task failed, succeded or is running.

To access the information about the run, you can click on **Run information**  to expend the div.


Challenge view - evaluation results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the results of the evaluation of the
challenge. He can have in a quick look the view of all partcipant's scores
amongst each other, and access more detailed results.

Moving the mouse over one participant's name will make it appear in bold
compare to the others in the graph. Clicking on |contestviewmenuevaluationresults.png|
on the table will redirect to the specified evaluation of the corresponding participant.

|contestviewevaluationresults.png|

Participant evaluation view
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each participant can access its own evaluation results. It correspond to
a page showing a graph with for each criterion the min and max score as
well as Participant score.

It is also possible to switch between normalized scores and raw scores
(not normalized) of the participant.

The user can also dowload a csv file containing all the results by
clicking on |evaluation.png|

Challenge view - ranking
^^^^^^^^^^^^^^^^^^^^^^^^

From this page, the user can access the ranking of the challenge (note
this page is also visible without being logged, but some information may
be not visible in that case).

|contestviewranking.png|

Settings - Manage Data Series
-----------------------------

From the Settings button on the top menu bar, select **Manage Series** . The list of
existing series will appear. To create a new one click on **Add Data Series** .

Once all the fields filled, save by clicking **Insert** .

|seriescreation.png|

.. |contestcreated.png| image:: includes/sum/contest_created.png
.. |contestpromoted.png| image:: includes/sum/contest_promoted.png
.. |contestopen.png| image:: includes/sum/contest_open.png
.. |contestinprogress.png| image:: includes/sum/contest_in_progress.png
.. |contestonevaluation.png| image:: includes/sum/contest_on_evaluation.png
.. |contestclosed.png| image:: includes/sum/contest_closed.png
.. |settings.png| image:: includes/sum/settings.png
.. |homepage.png| image:: includes/sum/homepage.png
.. |userinfo.png| image:: includes/sum/user_info.png
.. |userprofile.png| image:: includes/sum/user_profile.png
.. |certifupload.png| image:: includes/sum/certif_upload.png
.. |createcontest.png| image:: includes/sum/create_contest.png
.. |modify-icon.png| image:: includes/sum/modify-icon.png
.. |delete.png| image:: includes/sum/delete.png
.. |users.png| image:: includes/sum/users.png
.. |metrics.png| image:: includes/sum/metrics.png
.. |contestmodify.png| image:: includes/sum/contest_modify.png
.. |contestjoin.png| image:: includes/sum/contest_join.png
.. |contestviewmenu.png| image:: includes/sum/contestview_menu.png
.. |contestviewmenuhome.png| image:: includes/sum/contestview_menu_home.png
.. |contestviewmenudatapackage.png| image:: includes/sum/contestview_menu_datapackage.png
.. |contestviewmenuusers.png| image:: includes/sum/contestview_menu_users.png
.. |contestviewmenuenvironments.png| image:: includes/sum/contestview_menu_environments.png
.. |contestviewmenucriteria.png| image:: includes/sum/contestview_menu_criteria.png
.. |contestviewmenuapplications.png| image:: includes/sum/contestview_menu_applications.png
.. |contestviewmenumetrics.png| image:: includes/sum/contestview_menu_metrics.png
.. |contestviewmenuevaluationresults.png| image:: includes/sum/contestview_menu_evaluationresults.png
.. |contestviewmenuranking.png| image:: includes/sum/contestview_menu_ranking.png
.. |contestviewdescription.png| image:: includes/sum/contestview_description.png
.. |contestviewdatapackageparticipant.png| image:: includes/sum/contestview_datapackage_participant.png
.. |deleteenv.png| image:: includes/sum/delete_env.png
.. |contestviewdatapackageinitiator.png| image:: includes/sum/contestview_datapackage_initiator.png
.. |contestviewusers.png| image:: includes/sum/contestview_users.png
.. |contestviewenvironments.png| image:: includes/sum/contestview_environments.png
.. |dashboard.png| image:: includes/sum/dashboard.png
.. |oozie.png| image:: includes/sum/oozie.png
.. |dashboardpage.png| image:: includes/sum/dashboard_page.png
.. |oozieMonitor.png| image:: includes/sum/oozieMonitor.png
.. |contestviewapplicationsparticipant.png| image:: includes/sum/contestview_applications_participant.png
.. |appref.png| image:: includes/sum/appref.png
.. |updateappref.png| image:: includes/sum/update_appref.png
.. |contestviewapplicationsparticipant2.png| image:: includes/sum/contestview_applications_participant2.png
.. |contestviewapplicationsadmin.png| image:: includes/sum/contestview_applications_admin.png
.. |appevalref.png| image:: includes/sum/appevalref.png
.. |updateevalref.png| image:: includes/sum/update_evalref.png
.. |contestviewapplicationsevaluator.png| image:: includes/sum/contestview_applications_evaluator.png
.. |contestviewevaluationtreeevaluator.png| image:: includes/sum/contestview_evaluationtree_evaluator.png
.. |contestviewevaluationtreeparticipant.png| image:: includes/sum/contestview_evaluationtree_participant.png
.. |contestviewmetrics.png| image:: includes/sum/contestview_metrics.png
.. |contestviewscores.png| image:: includes/sum/contestview_scores.png
.. |contestviewlinguisticterms.png| image:: includes/sum/contestview_linguisticterms.png
.. |contestviewevaluationresults.png| image:: includes/sum/contestview_evaluationresults.png
.. |contestviewranking.png| image:: includes/sum/contestview_ranking.png
.. |search.png| image:: includes/sum/search.png
.. |bbox2.png| image:: includes/sum/bbox2.png
.. |bbox1.png| image:: includes/sum/bbox1.png
.. |datapackageitemmanagement.png| image:: includes/sum/datapackage_item_management.png
.. |csvdownload.png| image:: includes/sum/csv_download.png
.. |evaluation.png| image:: includes/sum/evaluation.png
.. |controlpanel.png| image:: includes/sum/controlpanel.png
.. |usermanagement.png| image:: includes/sum/user_management.png
.. |accept.png| image:: includes/sum/accept.png
.. |denied.png| image:: includes/sum/denied.png
.. |participantmanagement.png| image:: includes/sum/participant_management.png
.. |usermanagement3.png| image:: includes/sum/user_management3.png
.. |seriescreation.png| image:: includes/sum/series_creation.png
.. |manageenvironment.png| image:: includes/sum/manage_environment.png
.. |stopenv.png| image:: includes/sum/stop_env.png
.. |startenv.png| image:: includes/sum/start_env.png
.. |newcriterion.png| image:: includes/sum/new_criterion.png
.. |deletecriterion.png| image:: includes/sum/delete_criterion.png
.. |newcriterionDescription.png| image:: includes/sum/new_criterion_Description.png
.. |criterionpage.png| image:: includes/sum/criterion_page.png
.. |htmlsupport.png| image:: includes/sum/html_support.png
.. |htmlsupport2.png| image:: includes/sum/html_support2.png
.. |bell.png| image:: includes/sum/bell.png
.. |notifications.png| image:: includes/sum/notifications.png
.. |rssfeed.png| image:: includes/sum/rssfeed.png
.. |notificationsfeed.png| image:: includes/sum/notifications_feed.png
.. |metricsxml.png| image:: includes/sum/metricsxml.png
.. |scoresxml.png| image:: includes/sum/scoresxml.png
.. |scorescsv.png| image:: includes/sum/scorescsv.png
.. |scorecsvtext.png| image:: includes/sum/scorecsvtext.png
