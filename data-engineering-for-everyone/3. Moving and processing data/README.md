# Moving and processing data

## Proceesing data

### Connect the dots

Data pipelines are used to process data. At the end of Chapter 1, you learned about ETL (Extract, Transform, Load), one of the frameworks used to build data pipelines. The data processing tasks you just studied actually match that framework, corresponding to either extraction, transformation or loading operations.

Note that although saving and loading are usually considered to be opposites, in the context of data engineering, they are the same thing, as you may have noticed. The reason for this is that when you're saving something, you're just storing it in the next step in the pipeline.

Can you correctly classify data processing tasks as extraction, transformation, or loading operations?

Extract

- Collecting data from Google Analytics about our web-marketing promotion offering 3 months of access the premium tier
- Pulling the top 20 songs users have been listening to on a loop

Transform

- Sorting a playlist's songs based on the date they were added
- Summarizing the yearly listening activity to tell users how many hours they've listened to music on Spotflix this year

Load

- Saving the new order of a playlist that was sorted based on the date songs were added, so that it remains that way the next time the user connects
- Writing all the followers of a user in a table

## Scheduling data

### Schedules

You just saw three ways of scheduling data: manually, at a specific time, or if a specific condition is met.

Can you correctly classify the actions on the right?

Manual

- Running the song encoding pipline, because engineering changed the encoder and wants to make sure they still pass the validation check
- Running the pipeline processing sign ups because in the past 10 minutes, 100 new users complained to support that they can't connect

Time

- Generating the Spotflix Weekly Playlist from Chapter 1 every Monday at 00:00 AM
- Processing music, videos uploads by artist every hour
- Collecting data from Google Analytics every morning to check how the promotion compaign is going

Condition

- Running validation checks if new videos are being collected
- Updating the number of followers in a playlist table a user subcribed to it

### One or the other

You've seen that data can be processed in batches (records are grouped and processed at intervals) or streams (records are sent individually right away).

Can you correctly classify the actions on the right as being batched or streamed?

Some of these are tricky, you may have to think twice! Don't worry if you don't get it right the first time. All that matters is that you get the difference between batches and streams, so if you make a mistake, make sure to read the orange feedback messages at the bottom left to understand why!

Batch

- Loading new employees to Spotflix's employee table
- Reducing access to premium features when someone unsubscribes

Stream

- Updating the count of followers in a playlist when a user subcribes to it
- When a user listen to songs that are being recommended in real time, loading his upvotes and downvotes on each song

## Parallel computing

### Whenever, whenever

While you're having lunch with the rest of the data science team, Sasha, the new data engineer intern, is telling you this: "Parallel computing is a jack of all trades and can be used whenever we want, for any task we want. It just optimizes running any data processing tasks. We should start implementing it across the whole pipeline. I'm ready to help doing it!"

Is her statement actually true or false?

Possible Answers: False

### Parallel universe

You just told Sasha, the data engineer intern, that although incredibly efficient and powerful, parallel computing is not suited to every situation. It has its limitations, and sometimes it's just unnecessary.

You would like to help Sasha improve her understanding. You ask her to tell you their assumptions about parallel computing: you will tell her if she's right or wrong, and try to explain why. Are you up to the challenge?

Right

- Parallel computing relles on processing units
- It's a good idea to use parallel computing to encode songs uploaded by artist to the .ogg format that Spotflix prefers
- Parallel computing is used to provide extra processing power

Wrong

- Parallel computing will always make things faster
- Parallel computing can't be used to optimize for memory usage
- It's a good idea to use parallel computing to update the employee tabe every morning

## Cloud computing

### Obscured by clouds

Sasha, the new data engineer intern, is now trying to convince you that cloud computing and multicloud computing have absolutely no downsides. You disagree: you know for a fact that this is not true. It makes you question whether or not she is actually comfortable with the topic.

Once again, you take your manager role to heart and try to help her improve her understanding. You ask her to tell you their assumptions about cloud computing: you will tell her if she's right or wrong, and try to explain why. Are you up to the challenge?

Right

- Leveraging the cloud instead of having our own-premises data center allows us to use just resources we nee, when we need them
- A multicloud solution reduces rellance on a single vector
- Cloud computing encompassed storage, database and computing solutions

Wrong

- Cloud computing reduces all kinds of risk
- EC3, S3 and RDS are solutions offered by Microsoft Azure
- Multicloud solution reduce security and govermance concerns

### Somewhere I belong

81% of companies have implemented a multicloud approach, according to Gartner. Spotflix's data engineers are worried about the company's reliance on a single vendor, and are considering a multicloud approach. They also think it might be allow Spotflix to reduce costs, and to be more resilient in the face of a disaster.

As you've just seen, the main cloud providers are AWS, Microsoft Azure and Google Cloud. Together, they own about half of the cloud computing market share. They have different services, some you saw in the video, some you're about to discover. They also have competitors, some of which you're about to discover as well.

Can you help the data engineers classify the different services before they start evaluating alternatives?

File storage

- IBM Cloud File Storage
- AWS S3

Computing

- Azure Virtual Machine
- AWS EC2

Databases

- Snowflake Data Warehouse
- AWS Redshift (Data ware house)
- Google Cloud Database (NoSQL)
