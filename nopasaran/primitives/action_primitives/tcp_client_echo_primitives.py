from nopasaran.decorators import parsing_decorator
from nopasaran.definitions.events import EventNames
import nopasaran.utils as utils

class TCPClientEchoPrimitives:
    """
    Class containing a one-shot TCP Echo client method for the state machine.
    """

    @staticmethod
    @parsing_decorator(input_args=4, output_args=1)
    def make_tcp_echo_request(inputs, outputs, state_machine):
        """
        A one-shot TCP echo request, analogous to make_http_1_request.

        Number of input arguments: 4
            1) ip
            2) port
            3) message
            4) timeout

        Number of output arguments: 1
            1) response (the echoed result or None)

        This method:
         - Creates a socket
         - Connects to (ip, port)
         - Sends `message`
         - Receives the echo
         - Closes the socket
         - Triggers RESPONSE_RECEIVED if successful, or REQUEST_ERROR if None
        """
        ip      = state_machine.get_variable_value(inputs[0])
        port    = int(state_machine.get_variable_value(inputs[1]))
        message = state_machine.get_variable_value(inputs[2])
        timeout = float(state_machine.get_variable_value(inputs[3]))

        response = utils.send_echo_once(ip, port, message, timeout)
        
        if response is not None:
            state_machine.trigger_event(EventNames.RESPONSE_RECEIVED.name)
        else:
            state_machine.trigger_event(EventNames.REQUEST_ERROR.name)
        
        # Store the echoed response (or None)
        state_machine.set_variable_value(outputs[0], response)
