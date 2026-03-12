<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">AI Chatbot with Personality</h3>

  <p align="center">
    A simple AI chatbot app with a settable personality, presented using a Gradio web interface
    <br />
  <!--  <a href="https://github.com/PensiveEagle/ai-chat-bot"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/ai-chat-bot">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/ai-chat-bot/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/ai-chat-bot/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a training project to create a simple chatbot that has a settable personality.

It uses the Gemini LLM, the langchain package, and a Gradio web interface.

It is Dockerised for easy deployment

<img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/ai-chat-bot/chatbot-screanshot.png" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Docker][docker-shield]][docker-url]
[![Python][python-shield]][python-url]
[![Gradio][gradio-shield]][gradio-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Docker
* Gemini API Key

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/ai-chat-bot.git
   ```
3. Create a `.env` file at the app root. E.G. `ai-chat-bot/.env`
4. Enter your Gemini API KEY in `.env`
   ```
   GEMINI_API_KEY=ENTER YOUR API KEY
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/ai-chat-bot
   git remote -v # confirm the changes
   ```
6. Build the docker image
   ```sh
   docker build -t ai-chatbot-app .
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the app:
1. Navigate to the app directory
2. Run a docker container off the image
   ```sh
   docker run --rm -d --env-file ./.env -p 7860:7860 --name chatbot-1 ai-chatbot-app
   ```
3. The application should be available in your browser at `localhost:7860`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/ai-chat-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/ai-chat-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/ai-chat-bot.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/ai-chat-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/ai-chat-bot.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/ai-chat-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/ai-chat-bot.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/ai-chat-bot/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/ai-chat-bot.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/ai-chat-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[product-screenshot]: images/screenshot.png
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[gradio-shield]: https://img.shields.io/badge/gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white
[gradio-url]: https://www.gradio.app/