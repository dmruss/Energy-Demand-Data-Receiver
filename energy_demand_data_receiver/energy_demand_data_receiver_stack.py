from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
    aws_lambda_python_alpha
    # aws_sqs as sqs,
)
from constructs import Construct

class EnergyDemandDataReceiverStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "EnergyDemandDataReceiverQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        fn = aws_lambda_python_alpha.PythonFunction(self, 
            "EnergyDemandDataReceiver",
            entry="./src",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            index="main.py",
            handler="lambda_handler"
        )

