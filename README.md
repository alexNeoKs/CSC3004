<div align="center">
 

  <h3 align="center"><b>CSC3004</b></h3>

  <p align="center">
    The therapy Application to end all Applications
    <br />
    <a href=""><strong>Click for the wiki »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- GETTING STARTED -->
## Getting Started
How to setup the current project.
### Prerequisites

Ensure that the docker image is built first
* cmd
  ```sh
  docker build -t chatserver .
  ```
### Installation

_Below is how you can install Kubernetes into the current system_
1. Install minikube from the link : https://minikube.sigs.k8s.io/docs/start/
2. Ensure that minikube.exe is inside environment path
3. In the terminal (either run cmd/powershell as admin) type _minikube start_
4. Enter _minikube dashboard_ to open up the dashboard
5. To move the docker image into minikube in the vs code terminal type "minikube docker-env | Invoke-Expression"
6. type "docker build -t chatserver ." to rebuild the image
7. type "minikube image ls" to check if image is inside
8. type "kubectl apply -f deployment.yaml"(do it for the rest of the yaml files too)
<br>
<p>
wait a few seconds and you should see it working in the dashboard
<p>enable loadbalancing service, open another cmd in admin mode and type "minikube tunnel --cleanup" (must leave this running)</>
</p>

# more info here -> https://minikube.sigs.k8s.io/docs/start/
# loadbalancer -> https://minikube.sigs.k8s.io/docs/handbook/accessing/#using-minikube-tunnel




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/alexNeoKs/CSC3004/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/alexNeoKs/CSC3004/forks
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
