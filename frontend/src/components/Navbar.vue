<!-- src/components/Navbar.vue -->
<template>
  <nav class="navbar">
    <div class="logo">
      <img src="@/assets/logo1.png" alt="Logo" />
      <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span>
    </div>
    <div class="nav-links">
      <router-link to="/register-influencer">
        <button>Register as Influencer</button>
      </router-link>
      <router-link to="/register-brand">
        <button>Register as Brand</button>
      </router-link>
      <router-link to="/about">
        <button>About</button>
      </router-link>
      <router-link to="/login">
        <button>Login</button>
      </router-link>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color:none;
}

.logo img {
  height: 50px;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

button {
  padding: 0.5rem 1rem;
  background-color: #31572c;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius:18px
}

button:hover {
  background-color: #99582a;
}
</style>