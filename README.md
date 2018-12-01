# Link Preview API

![python](https://img.shields.io/badge/Python-3.65-blue.svg?logo=python&longCache=true&logoColor=white&colorB=23a8e2)
![Pip](https://flat.badgen.net/pypi/v/pip?colorB=23a8e2)
![requests](https://img.shields.io/badge/requests-2.19.1-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2)
![flask](https://img.shields.io/badge/flask-1.0.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=23a8e2)
![beauitfulsoup](https://img.shields.io/badge/beautifulsoup4-4.6.3-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=23a8e2)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square)
[![GitHub issues](https://img.shields.io/github/issues/toddbirchard/Link-Preview-API.svg?style=flat-square)](https://github.com/toddbirchard/ghosttheme-stockholm/issues)
[![GitHub stars](https://img.shields.io/github/stars/toddbirchard/Link-Preview-API.svg?style=flat-square)](https://github.com/toddbirchard/ghosttheme-stockholm/stargazers?colorB=e3bb18)
[![GitHub forks](https://img.shields.io/github/forks/toddbirchard/Link-Preview-API.svg?style=flat-square)](https://github.com/toddbirchard/ghosttheme-stockholm/network)

![Link Preview](https://raw.githubusercontent.com/toddbirchard/Link-Preview-API/master/img/linkpreview.png)

## Usage

Public access currently not available, but considered.

**Link Preview API** consists of a single endpoint which acccepts a `?url=` parameter (we are assuming you are generating link previews for URLs you own). A successful request will parse the target URL for links in the article body and output JSON objects for each detected `<a>` tag. This JSON can be used to format HTML link previews to embed on the URL, thereby creating a better visual experience as well as countless SEO benefits:

```
[{
  "title": "GitHub launches Actions to execute code in containers and security alerts for Java and .NET projects | VentureBeat",
  "description": "GitHub introduced Actions for automated workflows and code execution in containers on GitHub, alongside other changes to the developer platform.",
  "image": "https://venturebeat.com/wp-content/uploads/2018/10/UPDATED-Actions-blog-screenshot-1.png?w=600",
  "sitename": "VentureBeat",
  "url": "https://venturebeat.com/2018/10/16/github-launches-actions-to-execute-code-in-containers-and-security-alerts-for-java-and-net-projects/"
}, {
  "title": "The Onion\u2019s Guide To Blockchain Technology",
  "description": "Blockchain technology forms the foundation for cryptocurrencies such as Bitcoin, Dogecoin, and Ethereum, but it can be difficult to understand how it actually works. The Onion answers common questions about blockchain technology.",
  "image": "https://i.kinja-img.com/gawker-media/image/upload/s--lOF4ZoeR--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/jn6fdwajhx8ihi47gsws.jpg",
  "sitename": "The Onion",
  "url": "https://www.theonion.com/the-onion-s-guide-to-blockchain-technology-1829819640"
}, {
  "title": "When courtroom science goes wrong \u2014 and how stats can fix it\n",
  "description": "COMIC: Bite marks, shoe prints, crime-scene fibers: Matches to suspects are often far shakier than courtroom experts claim. Better statistical methods \u2014 among them, a little beast known as the \u201clikelihood ratio\u201d \u2014 can cut down on wrong convictions.",
  "image": "https://www.knowablemagazine.org/sites/default/files/styles/1600_600/public/articles/167/court-forensics-comic-1600x600_1.png?itok=PNh8GH1i",
  "sitename": "Knowablemagazine",
  "url": "https://www.knowablemagazine.org/article/society/2018/when-courtroom-science-goes-wrong-and-how-stats-can-fix-it"
}, {
  "title": "Six Operational Advantages of Worker Cooperatives - Shareable",
  "description": "I am concerned that the economic advantages of organizing businesses as worker cooperatives are often forgotten, while idealistic goals often become the sole focus and motivation. Given the advantages available, worker cooperatives can be as competitive, if not more so, than any other type of business. What follows is an outline of these economic advantages. 1. Worker cooperatives can create jobs.",
  "image": "https://www.shareable.net/sites/default/files/blog/top-image/suma-group-pic1_0.jpg",
  "sitename": "Shareable",
  "url": "https://www.shareable.net/blog/six-operational-advantages-of-worker-cooperatives"
}]
```

## Functionality in Development

Returned in every response is a _sitename_. This site nme is compared against a list of the internet's top sources of content, thereby allowing us to serve bespoke embed styles for recognized sitenames nd ensure proper data extraction.
