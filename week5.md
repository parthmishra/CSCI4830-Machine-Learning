{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww13900\viewh13820\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #A. \
\
*T/F The VC-dimension is the maximum number of points that can be shattered in an infinite number of ways. Explain.*\
\
False, the VC-dimension refers to the maximum number of points that can be shattered *at all*. Not all sets of points can be shattered in an infinite number of ways i.e. there may be only one way to shatter some number of points, but that doesn\'92t change its dimensionality.\
\
*T/F SVMs, Naive Bayes, and logistic regression all find a hyperplane to separate data. Explain.*\
\
True, If we take hyperplane to be equivalent to \'93decision boundary/surface\'94 then all 3 satisfy this definition. All of them are linear classifiers that essentially form a hyperplane decision boundary via varying metrics.\
\
*Which has higher entropy? A rare word or a common word? Explain.*\
\
A rare word is more likely to have higher entropy due to the fact that more information is gained from a new, rare word compared to an common word. The frequency of a common word dilutes its information gain compared to the scarcity of a rare word, thus a rare word gives more information gain.\
\
*What is a Rademacher variable, and what function does it serve in terms of determining Rademacher complexity?*\
\
Rademacher variable is a random variable that provides symmetry to a correlation function in determining Rademacher complexity. It\'92s essentially signal noise for the data. The complexity is determined by how well the hypothesis space fits the data with random noise.\
\
\
#B. \
\
Here is a table for the results using 2 different loss functions (hinge and logistic) with varying degrees of L2 Regularization:\
\
|          | No Regularization | L2 = 0.1 | L2 = 0.5 | L2 = 1 |\
|----------|-------------------|----------|----------|--------|\
| Hinge    | 91.21%            | 54.39%   | 48.53%   | 53.55% |\
| Logistic | 93.30%            | 55.23%   | 48.11%   | 53.97% |\
\
\
As indicated by these data, it seems like any amount of regularization applied decreases the accuracy substantially.\
\
\
#C. \
\
One project I\'92m in interested in working on is not listed in Kaggle. Essentially, the project is to use incoming tweet data obtained via the Twitter streaming API during the Presidential Debates and try to classify incoming tweets as belonging to a Trump supporter or a Clinton supporter and see what accuracy can be achieved. This could be pretty interesting since it\'92s just using tweet text data to classify someone as a follower for a particular candidate. This information could be extrapolated to predict whether someone who doesn\'92t follow either Trump or Hillary as a potential supporter for one or the other. Knowing how likely a random member of the public with no visible affiliation to a political party is extremely valuable information. Also, this could easily be done with a multitude of linear classifiers such as Naive Bayes. \
\
Another project that I saw on the Kaggle site is the World Development Indicators dataset. Analysis of this data set to find certain features might reveal some interesting facts about what factors beyond the usual GDP can lead to a country being classified as developing and developed. The most valuable features might lead to some insight on what areas need to be focused on for different countries.\
\
\
\
\
}