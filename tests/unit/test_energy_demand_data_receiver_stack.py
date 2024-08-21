import aws_cdk as core
import aws_cdk.assertions as assertions

from energy_demand_data_receiver.energy_demand_data_receiver_stack import EnergyDemandDataReceiverStack

# example tests. To run these tests, uncomment this file along with the example
# resource in energy_demand_data_receiver/energy_demand_data_receiver_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EnergyDemandDataReceiverStack(app, "energy-demand-data-receiver")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
