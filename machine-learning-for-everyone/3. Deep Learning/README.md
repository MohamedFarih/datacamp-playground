# Deep Learning

## Deep learning

### What is deep learning?

Deep learning applications are everywhere. Think of Google translating large blocks of text in a matter of seconds or your phone's photo gallery automatically recognizing faces.

Let's see how much you know about deep learning.

True

- More complex problems like image classification can be solved much faster by deep learning than by traditional machine learning
- Deep learning is a subfield of machine learning concerned with algorithms inspired by the structure and function of the brain called neural networks
- When there is lack of domain knowledge and you are nor sure of the exact features that need to be used, you should use deep learning

False

- Deep learning is always preferred oevr traditional machine learning
- The number of neurons in a neural network is limited
- You have to figure out the higer-level features yourself while training the data

### Should I use deep learning?

You work for a bank and want to help your company make smarter loans. You'd like to predict the probability of a borrower defaulting on a loan based on information in their application, such as their credit history, education level, income, and assets. This amount can then be used to determine the interest rate of the loan. You have hundreds of thousands of examples of loans from the past ten years.

For now, you just want to build a proof of concept on your laptop showing that there is some value in building this model. The performance doesn't have to be perfect just yet.

Based on this information, how should you solve this problem?

Possible Answers: Traditional machine learning

## Computer vision

### Image data

Your friend just texted you an image. However, when you open the message the content seems to be distorted. No worries, you have access to a pre-trained neural network that can restore any image.

Before you can pass the image to the neural network, it needs to be converted to numbers so that we have features to input. The image's resolution is 284 × 429 pixels. Remember, each color pixel is represented by three color channels (red, green, and blue).

How many features will be passed into the model for this color image?

![Image noise](ImageNoise.png)

You can use the R console on the right as a calculator.

Possible Answers: 365508

Explain: 284 × 429 pixels × 3 channels = 365508

### The process

In a bar you strike up a conversation with someone who turns out to be a data scientist at the self-driving car department of Tesla.

They start talking about one of the deep learning models they built a while ago. It was able to classify images of vehicles as cars or trucks. You discuss the process and at the end of the conversation you have a pretty good idea of what happened.

- The car images are transformed to numbers
- The pixel intensitles are fed into a neural networks
- Neurons will learn to detect edges
- Neurons will learn to more complex objects like wheels, doors, and windows
- Neurons will learn to detect shapes of vehicles
- The image is classified as a car or a truck

### Recognizing handwritten digits

Remember this from Chapter 1? As a reminder, there's a famous dataset called the MNIST that contains 70,000 images of handwritten digits from 0 to 9. On the right, we have a computer vision model trained on this dataset that attempts to recognize handwritten digits.

For this exercise, we've added an extra dropdown where you can try different types of machine learning. The first two, logistic regression and random forest, are traditional machine learning models. As you've learned, the third, neural networks, is used in deep learning.

Try drawing some digits to see how well each model recognizes your handwriting. Which is the best performing machine learning model?

Possible Answers: Neural networks

## Natural Language Processing

### Sentiment analysis

Sentiment Analysis is a Natural Language Processing methodology for quantifying how positive or negative the emotion expressed by a segment of text is. It is often used for automatically categorizing customer feedback messages or product reviews.

Below are four reviews of the movie "The Last Jedi". You can paste them in the Sentiment Analyzer on the right.

Which review is scored as the most negative by the sentiment analysis algorithm?

Possible Answers: This movie was a pointless, ugly, and plot-hole-riddled mess. All it served to do was crush all hope and destroy everything that remained of the Original Trilogy.

### Classifying machine learning tasks

By this point, you have seen a lot of different applications of machine learning. In this chapter, two special fields were discussed: computer vision and Natural Language Processing (NLP). Deep learning is particularly well-suited to solve these kinds of problems. Let's see if you can identify which use case belongs to which field.

Computer vision

- Building an applcation that takes pictures of all the items passing on  coveyor belt and detecting any defects
- Seaching for images on Google

NLP

- Parsing all tweets about an artiest;s latest album to get a feeling for the sentiment toward it
- Auto-complete predicting the word you are typing while texting
- Google Home understanding that you have asked it to turn on the lights

Traditional Machine Learning

- Predicting the temperature in New York tomorrow
- Clustering pre-pald telecom customer to identify patterns in terms of money spend in recharging, sending SMS, and browsing the internet

### Bag of words

In the field of Natural Language Processing, n-grams are a foundational way to make features from text. n-grams count the sequence of words and n indicates how many word(s) a sequence contains. For example, 2-grams, count the occurrence of two-word sequences.

In this exercise, you can input text and see what are the top 1-gram, 2-gram, and 3-gram features based on occurrence. If you're not sure what to enter, try some of these restaurant reviews:

```
The food was not great and the service could be faster.
```

```
I've seen a lot of bad reviews about this place, but it was not that bad. You get what you pay for!
```

Which of the following statements is true?

Possible Answers: As you increase the value of n, the occurrences of n-grams decreases.

## Limits of machine learning

### To black box or not to black box?

You are interested in machine learning applications in the health sector. You know that some of the tasks require a high accuracy but it's not that important to know what happens inside the model. Others require an Explainable AI approach because the rationale for each classification is important.

- Black Box
  - Extract information from medical journal articles
  - Classify images from mammograms as cancerous or non-cancerous

- Explainable AI
  - Predict whether or not a nurse is likely to quit within the next month
  - Provide a list of likely diagnoses, given a set of facts about a patient

### Spotting bias in machine learning

In the video, we learned about an AI-enabled recruiting software that preferred men because it learned from historical data when more men were hired. When we have models that affect peoples' lives, we need to carefully evaluate them for any discriminatory behavior that can be learned from historical data.

On the right, you have a model that attempts to predict whether someone will default on their loan. You can break down the resulting predictions, by different features like demographics and employment status. Play around with these features and see if you can find anything suspicious about who is predicted to default and who isn't.

Which feature(s) should be investigated more for potential bias before deploying the model?

- Race because there is a relatively large difference between African American/ Caucasian proportions in the "No" (32%/68%) and "Yes" (74%/26%) outcomes.
