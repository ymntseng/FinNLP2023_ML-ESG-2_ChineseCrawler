# FinNLP-2023 ML-ESG-2 Chinese Crawler

This repo provides the Chinese dataset of FinNLP@IJCNLP-AACL-2023 ML-ESG-2 shared task.

Also, we provide the web crawler for ESG news content from Business Today. （https://esg.businesstoday.com.tw/catalog/180686/）.


## Environment Requirements

- Python 3.8
- Pandas 2.0.0
- Scrapy 2.8.0
- Scrapy-splash 0.8.0
- Bs4 0.0.1

## Dataset
There are 1260 instances in train set, 140 instances in dev set, and 156 instances in test set. Note that we've already released train, dev and test set.

The label of this Multi-Lingual ESG Impact Type Identification shared task（Chinese ver.） is described as follows.
- 0 : *Opportunity (related to company)*
- 1 : *Risk (related to company)*
- 2 : *Cannot Distinguish (related to company)*
- 3 : *Related to ESG, but not related to company*
- 4 : *Not related to ESG topic*


## Usage
- First, you need to install the requirements.（Note that the training set has already in **data/**.）

```
pip install -r requirements.txt
```

- Then, you can crawl the news content with HTML tags and the clean news content of all urls in the training set by giving the argument `-a dataset=Train`, `-a dataset=Dev` or `-a dataset=Test`.


- Finally, you can easily output the result into json or csv files as follows. The output will have two new columns along with the four columns of training set, so the output data shape will be（# of news, 6）. 

    - news_content：clean news content
    - news_content_html：origin HTML tags of news content

```
scrapy crawl business_today -a dataset={dataset} -o {output.csv}
scrapy crawl business_today -a dataset={dataset} -o {output.json}
```

## Reference

Please refer to FinNLP@IJCNLP-AACL-2023 website for more details.

[FinNLP@IJCNLP-AACL-2023] Shared Task: Multi-Lingual ESG Impact Type Identification (ML-ESG-2)：https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp2023/home
