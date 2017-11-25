# PDF-Progress
This project can be used to track the progress of a  PDF over time from a repository.


# Installation

## Development Installation
* Clone the project.
* Use Anaconda:
	```bash
	$ conda env create --force -f dev_environment.yml
	$ source activate pdf-progress
	```
* Install project in development mode.  
	```bash
	$ python setup.py develop
	```

## Production Installation
* Clone the project
* Use default python / Anaconda
* `$ python setup.py install`


# Tests
* To run the tests:  
	```bash
	$ make test
	```


# Example Use

### Use console scripts
PDF-Progress console scripts are automatically added to `/anaconda3/envs/pdf-progress/bin/` or `/usr/local/bin` when the project is installed.

```bash
# Single process word-count
$ pdf-progress-wc <FILENAME.pdf>

# Multiprocess word-count
$ pdf-progress-wc-mp <FILENAME.pdf>
```
