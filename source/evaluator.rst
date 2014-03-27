Initiator Guide
================

Role description
----------------

An **evaluator** in E-CEO platform is the person in charge of the evaluation of a challenge. He is the one running and evaluating all applications of participants.
Challenge **evaluators** will use the platform to:

-  define challenge evaluation tree,
-  evaluate participant application,
-  get information about the Evaluation Environment

Challenge view
--------------

The challenge view contains all the different pages associated to a challenge. The accessible pages are not the same depending on the role of the challenge.
The pages are accessible from a vertical menu bar on the left.

The list of pages accessible for an **evaluator** are:

-  |contestviewmenuhome.png| Challenge description
-  |contestviewmenudatapackage.png| Data packages
-  |contestviewmenuenvironments.png| Environments
-  |contestviewmenucriteria.png| Criteria importance/weights
-  |contestviewmenuapplications.png| Participants applications
-  |contestviewmenumetrics.png| Evaluation metrics
-  |contestviewmenuevaluationresults.png| Evaluation results
-  |contestviewmenuranking.png| Ranking


Global description
^^^^^^^^^^^^^^^^^^

From the home page, the user can choose **My Challenges** in the menu bar and then click on the challenge name to select it.
The first page he will see is the challenge description page.

.. image:: includes/sum/contestview_description.png
	:align: center

Data packages
^^^^^^^^^^^^^

The list of Data packages accessible for the participant is displayed, including the items associated to this data package and the search link used inside the application.xml file of the user application.

.. image:: includes/sum/contestview_datapackage_participant.png
	:align: center

Environments
^^^^^^^^^^^^

From this page, the user can access information about its environments
(Initiator and Administrator can see all environments of the challenge,
but Evaluator and Participants can see only their environment).

.. image:: includes/sum/contestview_environments.png
	:align: center

For each environment, it is possible to access the dashboard |dashboard.png| as well as the oozie monitor |oozie.png|.
The dashboard contains all information about the environment.

.. image:: includes/sum/dashboard_page.png
	:align: center

The oozie monitor page list all runs associated to an environment, including information about each part of the workflow.

.. image:: includes/sum/oozieMonitor.png
	:align: center

For each node of the workflow, the color indicates if the task failed, succeded or is running.
To access the information about the run, you can click on **Run information** to expend the div.

Participants applications
^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the challenge view the application part contains the information about the applications the evaluator needs to evaluate.

First the Evaluator has to choose an Application Reference by clicking on |appevalref.png| (this correspond to the run the evaluator launched to evaluate the
application of the participant).

.. image:: includes/sum/update_evalref.png
	:align: center

The evaluator can **Quantify** the application (this will automatically apply the quantification process on the application) or set the application as **Manually Evaluated** (this means he manually edited the quantification scores from the portal or from the Evaluation environment) by clicking on the corresponding button.

.. image:: includes/sum/contestview_applications_evaluator.png
	:align: center

The Evaluator can also apply quantification on all applications (**Quantify all**) or set them all as manually quantified (**Quantify all (manually)**).

Once all applications are quantified, the evaluator can do the final step of the evaluation which is the normalization by clicking on
**Evaluate all**. This will normalize all applications together and create scores between 0 and 1 for each criterion. It will also apply selected weights on each criterion.

Criteria importance/weights
^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the challenge view, evaluation tree can be updated in the following way:

-  change weight of a specific criterion (selection with radio button),
-  add new criterion to the challenge, clicking **Include** (the criterion has to be created by the administrator,
-  remove existing criterion from the challenge, clicking **Exclude** (the criterion is only removed from the challenge, not at the global level).

.. image:: includes/sum/contestview_evaluationtree_evaluator.png
	:align: center
	
Evaluation metrics
^^^^^^^^^^^^^^^^^^

From this page, the Evaluator can trigger evaluation results, such as metrics and quantification scores.

Metrics are results from the run of the participant's application.
Evaluator can add new metrics which will be used for the evaluation process.

.. image:: includes/sum/contestview_metrics.png
	:align: center

Quantification scores are results from the quantification of the participant's application, taking metrics as an input. Scripts are also available on the Evaluation platform to do all these actions in a easiest way.

.. image:: includes/sum/contestview_scores.png
	:align: center

Linguistic Terms are key/value association made from the Evaluator to evaluate some criterion whose value is a string.

.. image:: includes/sum/contestview_linguisticterms.png
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

Each participant can access its own evaluation results. It correspond to a page showing a graph with for each criterion the min and max score as well as Participant score.

It is also possible to switch between normalized scores and raw scores (not normalized) of the participant.

The user can also dowload a csv file containing all the results by clicking on |evaluation.png|

Ranking
^^^^^^^

From this page, the user can access the ranking of the challenge (note
this page is also visible without being logged, but some information may
be not visible in that case).

.. image:: includes/sum/contestview_ranking.png
	:align: center

Evaluation tools
----------------

On the Evaluation environment, a list of tools is available to ease Evaluator's evaluation process.

eceo-addmetrics
^^^^^^^^^^^^^^^

Add a name/value element(s) into monitor/monitor.xml file of the specified run.

usage:
-  eceo-addmetrics -r <runId> -n <metricsName> -v <metricsValue>
-  eceo-addmetrics -r <runId> -f <metricsFile>

.. image:: includes/sum/metricsxml.png
	:align: center

eceo-addscore
^^^^^^^^^^^^^

Add a name/value element into monitor/scores.xml file of the specified run. Score is the result of quantification process.

usage:
-  eceo-addscore-r <runId> -n <scoreName> -v <scoreValue>
-  eceo-addscore-r <runId> -f <scoreFile>

.. image:: includes/sum/scoresxml.png
	:align: center

eceo-csvtoscore
^^^^^^^^^^^^^^^

Update the file monitor/scores.xml of the specified run using entries inside the csv. Score is the result of quantification process.

usage:
-  eceo-csvtoscore -f <csvFile>

.. image:: includes/sum/scorescsv.png
	:align: center

.. image:: includes/sum/scorecsvtext.png
	:align: center

eceo-csvtoxmlscore
^^^^^^^^^^^^^^^^^^

Create a list of scores-runID.xml files. Score is the result of quantification process.

Evaluator can then review them and upload them into the run folder using eceo-addscore command.

usage:
-  eceo-csvtoxmlscore -f <csvFile>

.. |contestviewmenuhome.png| image:: includes/sum/contestview_menu_home.png
.. |contestviewmenudatapackage.png| image:: includes/sum/contestview_menu_datapackage.png
.. |contestviewmenuenvironments.png| image:: includes/sum/contestview_menu_environments.png
.. |contestviewmenucriteria.png| image:: includes/sum/contestview_menu_criteria.png
.. |contestviewmenuapplications.png| image:: includes/sum/contestview_menu_applications.png
.. |contestviewmenumetrics.png| image:: includes/sum/contestview_menu_metrics.png
.. |contestviewmenuevaluationresults.png| image:: includes/sum/contestview_menu_evaluationresults.png
.. |contestviewmenuranking.png| image:: includes/sum/contestview_menu_ranking.png
.. |dashboard.png| image:: includes/sum/dashboard.png
.. |oozie.png| image:: includes/sum/oozie.png
.. |appevalref.png| image:: includes/sum/appevalref.png
.. |evaluation.png| image:: includes/sum/evaluation.png
