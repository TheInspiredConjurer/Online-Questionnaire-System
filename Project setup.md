# Project setup
This project has a frontend using `npm` as package manager, [Vue](https://vuejs.org/) as the javascript framework and [Tailwind](https://tailwindcss.com/) as the CSS framework. The backend is written in Python with [Django](https://www.djangoproject.com/) as the Python framework. 

In order to get everything up and running we'll need to install the latest node version together with `npm`, `npm` will then care about all other dependencies. 
For the backend, we'll need to create a virtual python environment in which we'll then install all backend dependencies

### Node & npm for the frontend
in case you don't have node installed already, I can recommend using [nvm](https://github.com/nvm-sh/nvm) a Node Version Manager. It allows installing and switching between node version quite easily. 

Install it by executing the command mentioned in [Installing and updating](https://github.com/nvm-sh/nvm#installing-and-updating).

After that installing the latest version is as easy as executing
```shell
nvm install
```

You can verify the successful installation by asking 
```shell
node --version
# -> should equal the latest node version, v18.10.0 when this document was created

npm --version
# -> should equal the latest npm version, 8.19.2 when this document was created
```

### Virtual python environment for the backend
TODO
