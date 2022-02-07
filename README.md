# Welcome to the `sexxie` homepage
## Security State Configuration Inspection Engine


This tool leverages cloud provider APIs to test the existing state of cloud environments.

Security policy compliance testing is executed in the "plugins" directory.

Plugins are invoked from the "sexxie.py" entrypoint, as a python subprocess, and expect a successful return code. Success over time for each plugin become useful chartable metrics. Plugin success is published as custom cloudwatch metric for security dashboards.

Due to the nature of this architecture, plugins are standalone programs and can be written in any language to test just about anything.

Plugins execute serially, based on numeric prefix.



Here is an example run:

`./sexxie.py --profile aws-account-auditor --plugins all`


SeXXie :: Security State Configuration Inspection Engine


Executing the following plugins:
```
[
  '001_cloudtrail.py',
  '002_configservice.py',
  '003_vpcflowlogs.py',
  '004_iam.py',
  '005_egress.py',
  '101_custom_lambda.py',
  '201_pipeline_resources.py`,
  '201_pipeline_actions.py`
]


001_cloudtrail.py plugin has returned success
   - AWS cloudtrail security policy - OK

002_configservice.py plugin has returned success
   - AWS configservice security policy - OK

003_vpcflowlogs.py plugin has returned success
   - VPCFlowLog security policy - OK

004_iam_policy.py plugin has returned success
   - IAM security policy - OK

005_egress.py plugin has returned success
   - Netork egress security policy - OK

101_custom_lambda.py plugin has returned success
   - lambdas conform to serverless security policy - OK

201_pipeline_resources.py plugin has return success
   - pipelines have passed security resource inspection - OK

202_pipeline_actions.py plugin has return success
   - pipelines have passed security action inspection - OK


If any plugins fail, sexxie returns error code. This can be used for advanced pipeline auto-remediation techniques. Perhaps an application should be automatically brought down, if/when the application security policies are out of compliance. Downtime may be less costly than security violation, breaches, and reputation.
