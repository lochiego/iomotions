# iomotions

This project provides useful utilities for interfacing with [iMotions](https://imotions.com/) software from third party
applications.

Initial support is intended for [oTree](http://otree.org/), a behavioral experiment software. Its chief goal is to 
enhance experiments where subjects are tracked using iMotions, making it simple to mark events surrounding page 
interactions.

Over time this repository may grow to provide more hooks to iMotions APIs.

## Installation
To use this module add the following line to your `requirements.txt` file:

```requirements.txt
iomotions>=0.0.1
```

Then install your requirements as usual.

```shell script
pip3 install -r requirements.txt
```

As usual it's recommended that you use a virtual environment for your dependencies.

### Usage

#### oTree Integration API

##### ScenePage
`ScenePage` makes it simple to send start and end scene markers to oTree. Subclass this type instead of `Page` and the
scene markers will use the class name as the scene description. When the page loads a start scene marker is sent to 
iMotions, and following a successful `Post` it will send the end scene marker, prior to progressing to the next page.

```python
from iomotions.otree.pages import ScenePage
...

class QuizPage(ScenePage):
    pass
```

If you would like to provide an alternative scene identifier than the class name, simply override the `scene_name` 
property with the string you would like to use instead.

```python
from iomotions.otree.pages import ScenePage
...

class QuizPage(ScenePage):
    scene_name = 'Question'
```

_Note_: The current round number will also be appended to the 
scene name to account for pages that appear in multi-round apps.

You can similarly specify a `scene_description` property to add the _Description_ property to the iMotions start scene marker.
