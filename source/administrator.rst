Administrator Guide
===================

Role description
----------------

An **administrator** in E-CEO platform will be in charge of administrating one or several challenges.
Challenge **administrators** will use the platform to:

-  set-up environments,
-  define series and data packages,
-  add new **initiator** user,
-  accept or reject users for a challenge,
-  validate participant applications

Note that **administrator** can also do all actions that **initiator** or **evaluator** can do. Please also refer to <initator> or <evaluator>.

Challenge view
--------------

The challenge view contains all the different pages associated to a challenge. The accessible pages are not the same depending on the role of the challenge.
The pages are accessible from a vertical menu bar on the left.

|image: challengeview\_menu.png|

The list of pages accessible are (with type of user who can access it):

-  |image: challengeview\_menu\_home.png| Challenge description
-  |image: challengeview\_menu\_datapackage.png| Data packages
-  |image: challengeview\_menu\_users.png| Challenge users
-  |image: challengeview\_menu\_environments.png| Environments
-  |image: challengeview\_menu\_criteria.png| Criteria importance/weights
-  |image: challengeview\_menu\_applications.png| Participants applications
-  |image: challengeview\_menu\_metrics.png| Evaluation metrics
-  |image: challengeview\_menu\_evaluationresults.png| Evaluation results
-  |image: challengeview\_menu\_ranking.png| Ranking

Challenge view (global description)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <initator>.

Challenge view - Data packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <initator>.

Data package items management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <initator>.

Challenge view - users
^^^^^^^^^^^^^^^^^^^^^^
Please refer to <initator>.

Challenge view - environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <initator>.

Challenge view - criteria importance/weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <evaluator>.

Challenge view - applications (Administrator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view, the application part contains the information about the applications the administrator needs to validate.

|image: challengeview\_applications\_admin.png|

The Administrator can then decide to **Validate the application** or **Discard the application** if he juges its not suitable for being evaluated, by clicking on the corresponding button.

Challenge view - metrics
^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <evaluator>.

Challenge view - evaluation results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <evaluator>.

Challenge view - ranking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please refer to <evaluator>.

Settings - Manage Users
^^^^^^^^^^^^^^^^^^^^^^^^

From the **Settings** |image: settings.png| from the menu bar, select **Manage User**.

To manage users for a challenge, if not selected, select the tab **Users by Challenges**.

|image: user\_management.png|

Click on **change** to change either the Initiator or the Evaluator of the challenge, and then select the user you want to choose.

Click on **manage** to accept or reject participants for a challenge. From there, you can Accept |image: accept.png| or Deny |image: denied.png| a user.

|image: participant\_management.png|

To manage users in general, if not selected, select the tab **All Users**.

From there it is possible to set a user as global Initiator (this user will have rights to create a new challenge).

|image: user\_management3.png|

Settings - Manage Data Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the **Settings** |image: settings.png| from the menu bar, select **Manage Series**. The list of existing series will appear. To create a new one click on **Add Data Series**.
Once all the fields filled, save by clicking **Insert**.

|image: series\_creation.png|

Settings - Manage Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the **Settings** |image: settings.png| from the menu bar, select **Manage** **Environments**.

|image: manage\_environment.png|

The Template Settings part allow to select the provider, virtual network and template for the challenge. These settings will be used when the environments are generated.
To create a new environment, click on **Create**.

It is also possible to stop |image: stop\_env.png|, resume |image: start\_env.png| or delete |image: delete\_env.png| an existing environment.

Settings - Manage Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^

From the control panel, select **Manage** **Criteria**.

The Administrator can manage the criteria (independently of challenges) from this page by creating new ones |image: new\_criterion.png| or deleting definitively existing ones |image: new\_criterion\_Description.png|.
The “Unit/Dimension” field is a list representing the unit of the value of the criterion.

The “Quantification” and “Normalization” fields are both meant to contain formulas. To write a formula, add “$$” in the beginning and in the end of the latex formula. The formula will be displayed on the right part.

The “Quantification\_logic” is the logic used for normalization of the value obtained after quantification. It can be chosen between “Higher is Better” and “Lower is Better”.

The “Actor” field indicates who is calculating the value of the criterion. It could be the system or the evaluator.
Save the new criterion by clickin on **Save Criterion**.
Clicking on **Show info / Modify Criteria** will open the Criteria view.

|image: criterion\_page.png|

.. |image: challenge\_created.png| image:: includes/sum/challenge_created.png
.. |image: challenge\_promoted.png| image:: includes/sum/challenge_promoted.png
.. |image: challenge\_open.png| image:: includes/sum/challenge_open.png
.. |image: challenge\_in\_progress.png| image:: includes/sum/challenge_in_progress.png
.. |image: challenge\_on\_evaluation.png| image:: includes/sum/challenge_on_evaluation.png
.. |image: challenge\_closed.png| image:: includes/sum/challenge_closed.png
.. |image: settings.png| image:: includes/sum/settings.png
.. |image: homepage.png| image:: includes/sum/homepage.png
.. |image: user\_info.png| image:: includes/sum/user_info.png
.. |image: user\_profile.png| image:: includes/sum/user_profile.png
.. |image: certif\_upload.png| image:: includes/sum/certif_upload.png
.. |image: create\_challenge.png| image:: includes/sum/create_challenge.png
.. |image: modify-icon.png| image:: includes/sum/modify-icon.png
.. |image: delete.png| image:: includes/sum/delete.png
.. |image: users.png| image:: includes/sum/users.png
.. |image: metrics.png| image:: includes/sum/metrics.png
.. |image: challenge\_modify.png| image:: includes/sum/challenge_modify.png
.. |image: challenge\_join.png| image:: includes/sum/challenge_join.png
.. |image: challengeview\_menu.png| image:: includes/sum/challengeview_menu.png
.. |image: challengeview\_menu\_home.png| image:: includes/sum/challengeview_menu_home.png
.. |image: challengeview\_menu\_datapackage.png| image:: includes/sum/challengeview_menu_datapackage.png
.. |image: challengeview\_menu\_users.png| image:: includes/sum/challengeview_menu_users.png
.. |image: challengeview\_menu\_environments.png| image:: includes/sum/challengeview_menu_environments.png
.. |image: challengeview\_menu\_criteria.png| image:: includes/sum/challengeview_menu_criteria.png
.. |image: challengeview\_menu\_applications.png| image:: includes/sum/challengeview_menu_applications.png
.. |image: challengeview\_menu\_metrics.png| image:: includes/sum/challengeview_menu_metrics.png
.. |image: challengeview\_menu\_evaluationresults.png| image:: includes/sum/challengeview_menu_evaluationresults.png
.. |image: challengeview\_menu\_ranking.png| image:: includes/sum/challengeview_menu_ranking.png
.. |image: challengeview\_description.png| image:: includes/sum/challengeview_description.png
.. |image: challengeview\_datapackage\_participant.png| image:: includes/sum/challengeview_datapackage_participant.png
.. |image: delete\_env.png| image:: includes/sum/delete_env.png
.. |image: challengeview\_datapackage\_initiator.png| image:: includes/sum/challengeview_datapackage_initiator.png
.. |image: challengeview\_users.png| image:: includes/sum/challengeview_users.png
.. |image: challengeview\_environments.png| image:: includes/sum/challengeview_environments.png
.. |image: dashboard.png| image:: includes/sum/dashboard.png
.. |image: oozie.png| image:: includes/sum/oozie.png
.. |image: dashboard\_page.png| image:: includes/sum/dashboard_page.png
.. |image: oozieMonitor.png| image:: includes/sum/oozieMonitor.png
.. |image: challengeview\_applications\_participant.png| image:: includes/sum/challengeview_applications_participant.png
.. |image: appref.png| image:: includes/sum/appref.png
.. |image: update\_appref.png| image:: includes/sum/update_appref.png
.. |image: challengeview\_applications\_participant2.png| image:: includes/sum/challengeview_applications_participant2.png
.. |image: challengeview\_applications\_admin.png| image:: includes/sum/challengeview_applications_admin.png
.. |image: appevalref.png| image:: includes/sum/appevalref.png
.. |image: update\_evalref.png| image:: includes/sum/update_evalref.png
.. |image: challengeview\_applications\_evaluator.png| image:: includes/sum/challengeview_applications_evaluator.png
.. |image: challengeview\_evaluationtree\_evaluator.png| image:: includes/sum/challengeview_evaluationtree_evaluator.png
.. |image: challengeview\_evaluationtree\_participant.png| image:: includes/sum/challengeview_evaluationtree_participant.png
.. |image: challengeview\_metrics.png| image:: includes/sum/challengeview_metrics.png
.. |image: challengeview\_scores.png| image:: includes/sum/challengeview_scores.png
.. |image: challengeview\_linguisticterms.png| image:: includes/sum/challengeview_linguisticterms.png
.. |image: challengeview\_evaluationresults.png| image:: includes/sum/challengeview_evaluationresults.png
.. |image: challengeview\_ranking.png| image:: includes/sum/challengeview_ranking.png
.. |image: search.png| image:: includes/sum/search.png
.. |image: bbox2.png| image:: includes/sum/bbox2.png
.. |image: bbox1.png| image:: includes/sum/bbox1.png
.. |image: datapackage\_item\_management.png| image:: includes/sum/datapackage_item_management.png
.. |image: csv\_download.png| image:: includes/sum/csv_download.png
.. |image: evaluation.png| image:: includes/sum/evaluation.png
.. |image: controlpanel.png| image:: includes/sum/controlpanel.png
.. |image: user\_management.png| image:: includes/sum/user_management.png
.. |image: accept.png| image:: includes/sum/accept.png
.. |image: denied.png| image:: includes/sum/denied.png
.. |image: participant\_management.png| image:: includes/sum/participant_management.png
.. |image: user\_management3.png| image:: includes/sum/user_management3.png
.. |image: series\_creation.png| image:: includes/sum/series_creation.png
.. |image: manage\_environment.png| image:: includes/sum/manage_environment.png
.. |image: stop\_env.png| image:: includes/sum/stop_env.png
.. |image: start\_env.png| image:: includes/sum/start_env.png
.. |image: new\_criterion.png| image:: includes/sum/new_criterion.png
.. |image: delete\_criterion.png| image:: includes/sum/delete_criterion.png
.. |image: new\_criterion\_Description.png| image:: includes/sum/new_criterion_Description.png
.. |image: criterion\_page.png| image:: includes/sum/criterion_page.png
.. |image: html\_support.png| image:: includes/sum/html_support.png
.. |image: html\_support2.png| image:: includes/sum/html_support2.png
.. |image: bell.png| image:: includes/sum/bell.png
.. |image: notifications.png| image:: includes/sum/notifications.png
.. |image: rssfeed.png| image:: includes/sum/rssfeed.png
.. |image: notifications\_feed.png| image:: includes/sum/notifications_feed.png
.. |image: metricsxml.png| image:: includes/sum/metricsxml.png
.. |image: scoresxml.png| image:: includes/sum/scoresxml.png
.. |image: scorescsv.png| image:: includes/sum/scorescsv.png
.. |image: scorecsvtext.png| image:: includes/sum/scorecsvtext.png
