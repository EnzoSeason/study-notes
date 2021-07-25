# Guide

## 1. Requirements clarifications

Asking questions about the exact scope of the problem we are trying to solve.

Design questions are mostly open-ended. That’s why clarifying ambiguities early in the interview becomes critical.

## 2. Data model definition

Defining the data model in the early part of the interview will **clarify how data will flow between different system components**.

The candidate should identify various system entities, how they will interact with each other, and different aspects of data management like storage, transportation, encryption, etc.

## 3. System interface definition

Define what **APIs** are expected from the system.

This will establish the **exact contract expected from the system** and ensure if we haven’t gotten any **requirements** wrong.

## 4. Scale estimation

Estimating the **scale** of the system we’re going to design.

This will also help later when we focus on scaling, partitioning, load balancing, and caching.

## 5. High-level design

Draw a **block diagram** with 5-6 boxes representing **the core components** of our system.

We should identify enough components that are needed to **solve the actual problem from end to end**.

## 6. Detailed design

The **interviewer’s feedback** should always guide us to what parts of the system need further discussion.

We should present **different approaches**, their **pros and cons**, and explain **why we will prefer one approach over the other**.

## 7. Identifying and resolving bottlenecks

Try to discuss **as many bottlenecks as possible** and **different approaches** to mitigate them.
