<template>
  <div class="flex flex-col">
    <div class="lower-shadow p-4 flex flex-col items-center">
      <div>
        <h1>Online questionnaire system</h1>
        <h2>Features</h2>
        <div>
          <h3>Here are the basic (functional) requirements that I intend to integrate into the website:</h3>
          <ol>
            <li>
              <span>There are 4 types of users who should be able to access the website:</span>
              <ul>
                <li>Admin -> Has unsrestricted access to the website.</li>
                <li>Teacher / Educator -> Can create, edit and delete questions and choices created by them.</li>
                <li>Student -> Can only view question and select choices.</li>
                <li>Guest -> Can view every question, but not edit or update anything. They can also not view any choices.</li>
              </ul>
            </li>
            <li>Every question can have at max 5 choices, out of which only one will be true.</li>
            <li>Every question can belong to more than one category. One category can also have multiple questions.</li>
            <li>A teacher can create a question_set which will consist of a set of questions in a single place. One teacher can create multiple question_sets.</li>
          </ol>
          <h3>Planned Features:</h3>
          <ol>
            <li>Sessions and cookies</li>
            <li>Option to send a pdf of a student's score card to their email after they complete a test.</li>
            <li>Generate a PDF of all the scorecards of a student for a particular month, year, academic-session, etc.</li>
          </ol>
        </div>
      </div>
    </div>
    <div class="flex flex-col items-center">
      <h3>Built with</h3>
      <div class="flex justify-around">
        <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" class=" m-4">
          <img class="w-16" :src="cssLogo" alt="css 3 logo"/>
        </a>
        <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" class="m-4">
          <img class="w-16" :src="htmlLogo" alt="html 5 logo"/>
        </a>
        <a class="m-4" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
          <img class="w-16" :src="javascriptLogo" alt="javascript logo"/>
        </a>
        <a class="m-4" href="https://vuejs.org/">
          <img class="w-16" :src="vueLogo" alt="vue logo"/>
        </a>
        <a class="m-4" href="https://tailwindcss.com/">
          <img class="w-16" :src="tailwindLogo" alt="tailwind logo"/>
        </a>
        <a class="m-4" href="https://www.python.org/">
          <img class="w-16" :src="pythonLogo" alt="python logo"/>
        </a>
        <a class="m-4" href="https://www.djangoproject.com/">
          <img class="w-16" :src="djangoLogo" alt="django logo"/>
        </a>
        <a class="m-4" href="https://www.postgresql.org/">
          <img class="w-16" :src="postgresLogo" alt="postgresql logo"/>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import cssLogo from '@/assets/icons/css3.svg'
import djangoLogo from '@/assets/icons/django.svg'
import htmlLogo from '@/assets/icons/html-5.svg'
import javascriptLogo from '@/assets/icons/javascript.svg'
import postgresLogo from '@/assets/icons/postgresql.svg'
import pythonLogo from '@/assets/icons/python.svg'
import tailwindLogo from '@/assets/icons/tailwind-css.svg'
import vueLogo from '@/assets/icons/vue-js.svg'
</script>
