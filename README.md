# iomotions

This (unofficial) project provides useful utilities for interfacing with [iMotions](https://imotions.com/) software from third party
applications.

## Installation

To use this module add the following line to your `requirements.txt` file:

```requirements.txt
iomotions>=0.1.0
```

Then install your requirements as usual.

```shell script
pip3 install -r requirements.txt
```

## iMotions Setup

**IMPORTANT:** In order for the following functions to work you must ensure that in *Global Preferences > API > Event Receiving* both *Enable event reception* and *Use TCP* are checked.

## API

### `iomotions` module

#### `start_scene_recording(ip_address, scene_name, scene_description = '')`

Instruct the *iMotions* instance running at the designated IP address to start recording a scene with the prescribed name and optional description.

#### `end_scene_recording(ip_address, scene_name)`

Instruct the *iMotions* instance running at the designated IP address to end its recording of the named scene.

#### `class EventEmitter`

Helper class that stores connection information and exposes a simpler messaging API. This class is not well supported but can be used to send messages over UDP in place of the default TCP behavior of the above APIs.

### `iomotions.otree` module

`iomotions` includes API for integrating with [oTree](http://www.otree.org/) out of the box. The provided `iomotions.otree.pages.ScenePage` class extends oTree's [Page](https://otree.readthedocs.io/en/latest/pages.html) to record the page as a Scene in *iMotions*.

#### `class ScenePage(otree.api.Page)`

The `ScenePage` class should be subclassed in place of oTree's `Page` when you want *iMotions* to record the page. By using a `ScenePage` *iMotions* records a scene starting when the page begins loading and ending when the page transitions. The scene name is derived from the class name by default the current round number.

##### `scene_name`

If you would like to provide an alternative scene identifier than the class name, simply override the `scene_name` property with the string you would like to use instead.

##### `scene_description`

When provided, the description will be included with the scene marker in *iMotions*.

##### Full Example

```python
# <app-name>/__init__.py
from iomotions.otree.pages import ScenePage
...

class QuizPage(ScenePage):
    
    # optional, would default to QuizPage<round_number>
    scene_name = 'Question'
    
    # optional
    scene_description = 'General knowledge question'
```

**Note:** The current round number will also be appended to the scene name to account for pages that appear in multi-round apps.

**Note:** For simplicity to the user the `ScenePage` class extends private functions from `Page`. The primary motivation for this is to avoid unexpected breakage from overriding `before_next_page` without calling `ScenePage`'s implementation. Since the overridden methods are private it's possible that a future version of oTree will result in changes that break this API.
