<!-- src/components/Footer.vue -->
<template>
  <footer class="footer">
    <div class="social-icons">
      <i class="fa-brands fa-google"><a href="https://www.google.com" target="_blank"></a></i>
      <i class="fa-solid fa-envelope"><a href="https://www.gmail.com" target="_blank"></a></i>
      <i class="fa-brands fa-linkedin"><a href="https://www.linkedin.com" target="_blank"></a></i>
      <i class="fa-brands fa-facebook"><a href="https://www.facebook.com" target="_blank"></a></i>
      <i class="fa-brands fa-instagram"><a href="https://www.instagram.com" target="_blank"></a></i>
    </div>
    <div class="footer-text">
      <p>help@adfluence.com | All rights reserved © 2024</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
.footer {
  background-color: black;
  color: white;
  padding: 1rem;
  text-align: center;
  margin-top: 10px;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.footer-text {
  margin-top: 1rem;
}
</style>