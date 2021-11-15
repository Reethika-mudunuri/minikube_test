Kubenetes Rules Validator
==

This is a python project that can be used to validate the following rules against a kubernetes cluster.

* Validate image prefixes
* Validate label keys
* Validate the pod age

I have tested this python application against a kubernetes cluster built using minikube locally.
This python application has been tested on `python 3.6` on linux.

Install
--

Clone the repo

```
git clone https://github.com/reethikamudunuri/minicube_test.git
```

Install all dependencies in an virtualenv

```
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

Run
--
To apply the rules.

```
cd kube_pod_rules_validator
python main.py
```

This will display the results of rules for each pod using pretty print to the console.

```
[   {   'pod': 'coredns-74ff55c5b-dztsw',
        'rule_evaluation': [   {'name': 'image_prefix', 'valid': False},
                               {'name': 'team_label_present', 'valid': False},
                               {'name': 'recent_start_time', 'valid': True}]},
    {   'pod': 'kubernetes-dashboard-968bcb79-mfx5m',
        'rule_evaluation': [   {'name': 'image_prefix', 'valid': False},
                               {'name': 'team_label_present', 'valid': False},
                               {'name': 'recent_start_time', 'valid': True}]}
]
```

Development & Testing
--

References
--
* [Future Improvements](docs/future-improvements.md)
* [What I learnt](docs/what-i-learnt.md)