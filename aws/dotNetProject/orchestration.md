# Orchestration

## Step functions

AWS Step Functions is a reliable service to **coordinate distributed components** and **analyze the flow of your distributed workflow**.

Step Functions is based on the concepts of **tasks** and **state machines**. You define state machines using the JSON-based Amazon States Language.

### State types

States can perform a variety of functions in your state machine:

- Do some work in your state machine (a Task state)

- Make a choice between branches of execution (a Choice state)

- Stop an execution with a failure or success (a Fail or Succeed state)

- Simply pass its input to its output or inject some fixed data (a Pass state)

- Provide a delay for a certain amount of time or until a specified time/date (a Wait state)

- Begin parallel branches of execution (a Parallel state)

- Dynamically iterate steps (a Map state)

Any state type other than the Fail type have the full control over the input and the output. You can control those using the “InputPath”, “ResultPath” and “OutputPath”.
