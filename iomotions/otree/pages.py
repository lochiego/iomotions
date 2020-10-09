from ._builtin import Page
from django.http import HttpRequest
from ..imotions import send_event


class ScenePage(Page):
    """
    Extends the oTree Page class to send start and end scene events to iMotions running on the subject's computer.

    Attributes:
        scene_name (str): provides the "Short Text" meaning for start/end markers sent to iMotions.
        scene_description (str): provides the "Description" sent to iMotions for the scene start marker.
    """

    @property
    def scene_name(self):
        """
        Denotes the scene name in iMotions common across all subjects. If omitted will default to the class name. The
        round number will be appended to the scene name when sent to iMotions to distinguish multi-round pages.
        :return: The class name unless overridden.
        """
        # default to the name of the class if omitted.
        return type(self).__name__
    
    @property
    def scene_description(self):
        """
        Contextualizes the scene for iMotions to assist data analysis.
        :return: An empty string unless overridden.
        """
        # description is not terribly important so just ignore it if omitted.
        return ''

    def get(self):
        """Extends the Page get to send the start scene message to iMotions."""
        # This is called when the page contents are loading, so there could be a couple microseconds
        # delay but it should be close enough
        self._send_imotions(f'M;2;;;{self.scene_name}{self.round_number};{self.scene_description};S;V\r\n')
        return super(ScenePage, self).get()

    def _record_page_completion_time(self):
        """Extends the internal API used by Page just prior to concluding Post handling."""
        """
        Using this internal API over before_next_page is to avoid need to call super in subclasses.
        """
        self._send_imotions(f'M;2;;;{self.scene_name}{self.round_number};;E;\r\n')
        return super(ScenePage, self)._record_page_completion_time()

    def _send_imotions(self, message):
        """Forwards a message to the iMotions instance running on the subject's computer."""
        send_event(self.request.META.get('REMOTE_ADDR'), message)
