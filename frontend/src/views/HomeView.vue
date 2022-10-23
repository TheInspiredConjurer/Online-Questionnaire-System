<template>
  <div class="flex flex-col">
    <div
      class="smooth-shadow-black dark:smooth-shadow-white p-4 flex flex-col items-center"
    >
      <h1>Online questionnaire system</h1>
      <h2>Planned Features</h2>
      <div class="flex justify-around">
        <information-card headline="User management">
          <ul>
            <li>Admin -> Has unrestricted access to the website.</li>
            <li>
              Teacher / Educator -> Can create, edit and delete questions and
              choices created by them.
            </li>
            <li>Student -> Can only view question and select choices.</li>
            <li>
              Guest -> Can view every question, but not edit or update anything.
              They can also not view any choices.
            </li>
          </ul>
        </information-card>

        <information-card headline="Complex question and category system">
          <ul>
            <li>
              Every question can have at max 5 choices, out of which only one
              will be true.
            </li>
            <li>
              Every question can belong to more than one category. One category
              can also have multiple questions.
            </li>
          </ul>
        </information-card>

        <information-card headline="Advanced student score management">
          <ul>
            <li>Session cookies</li>
            <li>
              Option to send a pdf of a student's score card to their email
              after they complete a test.
            </li>
            <li>
              Generate a PDF of all the scorecards of a student for a particular
              month, year, academic-session, etc.
            </li>
          </ul>
        </information-card>
      </div>
    </div>
    <div class="flex flex-col items-center">
      <h3>Built with</h3>
      <div class="flex justify-around">
        <logo-link
          :logo="cssLogo"
          link="https://developer.mozilla.org/en-US/docs/Web/CSS"
        />
        <logo-link
          :logo="htmlLogo"
          link="https://developer.mozilla.org/en-US/docs/Web/HTML"
        />
        <logo-link
          :logo="javascriptLogo"
          link="https://developer.mozilla.org/en-US/docs/Web/JavaScript"
        />
        <logo-link :logo="vueLogo" link="https://vuejs.org/" />
        <logo-link :logo="tailwindLogo" link="https://tailwindcss.com/" />
        <logo-link :logo="pythonLogo" link="https://www.python.org/" />
        <logo-link :logo="djangoLogo" link="https://www.djangoproject.com/" />
        <logo-link :logo="postgresLogo" link="https://www.postgresql.org/" />
      </div>
    </div>
  </div>
</template>

<script>
import cssLogo from '@/assets/icons/css3.svg'
import djangoLogo from '@/assets/icons/django.svg'
import htmlLogo from '@/assets/icons/html-5.svg'
import javascriptLogo from '@/assets/icons/javascript.svg'
import postgresLogo from '@/assets/icons/postgresql.svg'
import pythonLogo from '@/assets/icons/python.svg'
import tailwindLogo from '@/assets/icons/tailwind-css.svg'
import vueLogo from '@/assets/icons/vue-js.svg'
import InformationCard from '@/components/InformationCard.vue'
import LogoLink from '@/components/LogoLink.vue'

export default {
  components: {
    InformationCard,
    LogoLink
  },
  data() {
    return {
      cssLogo,
      djangoLogo,
      htmlLogo,
      javascriptLogo,
      postgresLogo,
      pythonLogo,
      tailwindLogo,
      vueLogo
    }
  }
}
</script>

<style scoped></style>
