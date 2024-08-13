<template>
  <div class="register-brand">
    <Navbar />
    <div class="content">
      <div class="description-card">
        <img src="https://img.freepik.com/free-vector/businessmen-with-suitcase-statistics-bar-gears_24640-45238.jpg?t=st=1719803675~exp=1719807275~hmac=d0bb8e8b66f359d71aaa2f06eba5603f5085a15a9b115f61a39d52cffc599f00&w=826" alt="App Description Image">
        <p>
          Our platform helps you measure your campaign's true influence. 
          Manage end-to-end influencer campaigns at scale, tap into niche audiences, 
          and streamline your influencer marketing efforts with our comprehensive tools.
        </p>
      </div>
      <div class="form-card">
        <div class="card-body">
          <h5 class="card-title">Register as Brand</h5>
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
              <label for="company_name">Company Name:</label>
              <input type="text" v-model="company_name" class="form-control" id="company_name" required>
            </div>
            <div class="form-group">
              <label for="industry">Industry:</label>
              <input type="text" v-model="industry" class="form-control" id="industry" required>
            </div>
            <div class="form-group">
              <label for="budget">Budget:</label>
              <input type="number" v-model="budget" class="form-control" id="budget" required>
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
  name: 'RegisterBrand',
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      company_name: '',
      industry: '',
      budget: '',
      role: 'sponsor',
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
          sponsor_details: {
            company_name: this.company_name,
            industry: this.industry,
            budget: this.budget,
            status:'pending'
          },
          role: this.role
        })
        .then(response => {
          if (response.status === 201) {
            alert( 'Your request has been sent to admin. Once approved, you can login.')
            this.$router.push('/login');
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
.register-brand {
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
}
</style>