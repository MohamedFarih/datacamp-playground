# What is data engineering

## Data engineering and big data

### Go with the flow

To understand what data engineers do, why they are necessary and the impact they have, you need to know how data flows through an organization.

Can you order the four steps of the data science workflow chronologically?

Workflow:

- Data collection and storage
- Data preparation
- Exploration and visualization
- Experimentation and prediction

### Not responsible

You recently joined the data science team as a manager for a music streaming company named Spotflix. It's a music platform that lets users stream songs, create playlists, follow artists, watch music videos and even look up lyrics!

One of your colleagues just walked to your desk. They just got hired, but they already know you're on the data team - after training with DataCamp, you've made a name for yourself pretty quick! They have a bunch of data tasks they need completed, and they want to make sure they ask the right person. You tell them you can help them identify what they should request from data engineers, and what they should not.

Can you deliver on this promise?

Data engineering tasks

- Gathering music consumption data from desktop and mobile sources
- Optimizing the customers databases for analysis
- Ensuring corrupted, unreadable music tracks are removed and don't end up facing customers

Not data engineering tasks

- Building a visualization to understand listening patterns by city
- Based on their listening behavior, predict which songs customers are likely to enjoy
- Running an experiment to identify the optimal search bar positioning in the app

### Big time

You saw how the advent of big data increased the demand for data engineers. As more data gets generated, at a higher rate, with a growing variety of formats, the need for people able to manage this data is soaring.

Which of the statements on the right are true, and which are false?

True

- Data types refer to the variety of the data
- Value refers to how actionable the data is

False

- Velocity refers to how big the data is
- Volume has to do with how trustworthy the data is
- Veracity refers how frequently the data is generated

## Data engineers vs. data scientists

### Tell me the truth

In 2012, IBM declared that 90% of the data in the world had been created in the past 2 years. That same year, the amount of digital data in the world first exceeded 1 zetabyte (1 billion terabytes). In 2020, we're expected to reach 44 zetabytes. This big data era led to the advent of two new roles: data engineers and data scientists. You just studied the differences between these two roles.

Let's have a quick sanity check: which of the following options is true?

Possible Answers: Data engineers enable data scientists.

### Who is it

In the first lesson, you classified some data related tasks between data engineer tasks and not data engineer tasks. Let's raise the bar and see if you can assign more specific tasks to data engineers or data scientists.

Data engineer

- Ensure that people who use the databases can't erase music videos by mistake
- Use Java to build a pipline collecting album covers and storing them
- Provide listening sessions data so it can be analyzed with minimal preparation work

Data Scientist

- Find out in which countries certain artist are popular to give them insights on where to tour
- Use Python to run an analysis and understand whether users prefer having the search bar on the top left or the top right of the Spotflix desktop app
- Identify which customers are likely to end their Spotflix subscriptions, so marketing can target them and encourage them to renew

## The Data pipline

### It's not true

The main objective, when setting up data pipelines, is to improve the efficiency with which data flows, from its ingestion to the final users.

Most of the options below are true, but one is false. Which one is it?

Possible Answers: Data pipelines necessarily include a transformation step.

### Pipeline

Once you've successfully completed this exercise, make sure to read the success message! 🎶😉

You've just seen some examples of pipelines used at Spotflix. Let's have you build one!

Our data engineer, Vivian, is working on building new pipelines to generate a new product: the Weekly Playlist. It's a playlist that is created by our system every day to recommend new songs that users might like based on their tastes.

On the right, you will find some steps. Can you order the steps correctly to help her build the pipeline generating a Weekly Playlist for each user? Let's start with one user, and build a pipeline to generate a Weekly Playlist for Julian, our data scientist.

- Extract the songs Julian listened to the most over the past month
- Find other users who listened to these same songs a lot as well
- Load only 10 tops songs these listened to the most over the past week into a table called "Similar profiles"
- Extract only songs these other users listen to that are of the same genre as the ones in Julian's listening sessions. These are our recommendations
- Load the recommended songs into a new table. That's Julian's Weekly Playlist
