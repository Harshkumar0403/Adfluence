<template>
  <div class="register-influencer">
    <Navbar />
    <div class="content">
      <div class="description-card">
        <img src="https://img.freepik.com/free-vector/influencer-video-blogging-illustration_23-2148642925.jpg?t=st=1719803645~exp=1719807245~hmac=e4445c6c43f76dcc16a5c7fc270e36148cbbcf0bd18f0f8901159d3e4470bc75&w=740" alt="App Description Image">
        <p>
          Our platform helps you measure your campaign's true influence. 
          Manage end-to-end influencer campaigns at scale, tap into niche audiences, 
          and streamline your influencer marketing efforts with our comprehensive tools.
        </p>
      </div>
      <div class="form-card">
        <div class="card-body">
          <h5 class="card-title">Register as Influencer</h5>
          <form @submit.prevent="register">
            <div class="form-group">
              <label for="username">Username:</label>
              <input type="text" v-model="username" class="form-control" id="username" required>
            </div>
            <div class="form-group">
              <label for="email">Email:</label>
              <input type="email" v-model="email" class="form-control" id="email" required>
            </div>
            <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" v-model="password" class="form-control" id="password" required>
            </div>
            <div class="form-group">
              <label for="category">Category:</label>
              <input type="text" v-model="category" class="form-control" id="category" required>
            </div>
            <div class="form-group">
              <label for="niche">Niche:</label>
              <input type="text" v-model="niche" class="form-control" id="niche" required>
            </div>
            <div class="form-group">
              <label for="reach">Reach:</label>
              <input type="number" v-model="reach" class="form-control" id="reach" required>
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
            <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
          </form>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from 'axios';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'RegisterInfluencer',
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      category: '',
      niche: '',
      reach: '',
      role: 'influencer',
      errorMessage: ''
    };
  },
  methods: {
    register() {
      if (this.password.length < 5 || this.password.length > 10) {
        this.errorMessage = 'Password must be between 5 and 10 characters long';
        return;
      }

      axios
        .post('http://127.0.0.1:5000/api/register', {
          username: this.username,
          email: this.email,
          password: this.password,
          influencer_details: {
            category: this.category,
            niche: this.niche,
            reach: this.reach
          },
          role: this.role
        })
        .then(response => {
          if (response.status === 201) {
            localStorage.setItem('authToken', response.data.token);
            localStorage.setItem('email', response.data.email);
            localStorage.setItem('user_id', response.data.user_id);
            localStorage.setItem('influencer_id', response.data.influencer_id);
            localStorage.setItem('username', response.data.username);
            localStorage.setItem('category', response.data.category);
            localStorage.setItem('niche', response.data.niche);
            localStorage.setItem('reach', response.data.reach);
            localStorage.setItem('role', response.data.role);
            this.$router.push('/influencer-dashboard');
          }
        })
        .catch(error => {
          console.log(error);
          this.errorMessage = 'Registration failed. Please try again.';
        });
    }
  }
};
</script>

<style>
.register-influencer {
  background-color: #f5ebe0;
}

.content {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.description-card {
  background-color: #fff;
  color: #000;
  width: 70vw;
  padding: 20px;
  margin-right: 10px;
  border-radius: 18px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.description-card img {
  max-width: 100%;
  height: auto;
  border-radius: 18px;
}

.form-card {
  background-color: #9f7e69;
  color: white;
  width: 30vw;
  padding: 20px;
  border-radius: 18px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
