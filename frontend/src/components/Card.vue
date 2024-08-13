<!-- src/components/Card.vue -->
<template>
  <div class="card">
    <h2>{{ heading }}</h2>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  props: {
    heading: String,
    message: String
  }
};
</script>

<style scoped>
.card {
  background-color: #9f7e69;
  border-radius: 18px;
  padding: 20px;
  margin: 10px 0;
  width: 50vw;
  font-family: 'Roboto', sans-serif;
  color: #ffffff;
}
h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}
p {
  font-size: 1em;
}
</style>
