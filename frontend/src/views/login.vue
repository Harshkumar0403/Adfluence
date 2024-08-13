<template>
  <div class="login">
    <Navbar />
    <div class="content">
      <div class="card-container">
        <div class="card info-card">
          <img class="card-img-top" src="https://img.freepik.com/free-vector/business-team-brainstorm-idea-lightbulb-from-jigsaw-working-team-collaboration-enterprise-cooperation-colleagues-mutual-assistance-concept-pinkish-coral-bluevector-isolated-illustration_335657-1651.jpg?t=st=1719737943~exp=1719741543~hmac=311555c33b97aea5793fb508d8db9a28b5245839d7c7c557dde9deb6f17a09cf&w=996" alt="Card image cap">
          <div class="card-body">
            <h2 class="card-title" style="color:#283618;font-family:Times-New-Roman"><b>Welcome to Adfluence</b></h2>
            <p class="card-text" style="color:#e3d5ca">A full stack solution to manage end-to-end influencer campaigns at scale.</p>
          </div>
        </div>
        <div class="card form-card">
          <div class="card-body">
            <h5 class="card-title">Login</h5>
            <form @submit.prevent="login">
              <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" v-model="email" class="form-control" id="email" required>
              </div>
              <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" v-model="password" class="form-control" id="password" required>
              </div>
              <button type="button" class="btn btn-primary" style="border-radius:10px;background-color:#31572c" @click="login">Login</button>
              <button type="button" class="btn btn-secondary" style="margin-left:4px;border-radius:10px" @click="adminLogin">Admin Login</button>
            </form>
            <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
          </div>
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
  name: 'Login',
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    
    login() {
  axios
    .post('http://127.0.0.1:5000/api/login', {
      email: this.email,
      password: this.password
    })
    .then(response => {
      if (response.status === 200) {
        localStorage.setItem('authToken', response.data.token);
        localStorage.setItem('username', response.data.username);
        localStorage.setItem('user_id', response.data.user_id);
        localStorage.setItem('email', response.data.email);
        localStorage.setItem('role', response.data.role);
        let role = response.data.role;
        if(role == 'sponsor' && response.data.status=='approved') {
          localStorage.setItem('Company_name', response.data.Company_name);
          localStorage.setItem('sponsor_id', response.data.sponsor_id);
          localStorage.setItem('Industry', response.data.Industry);
          localStorage.setItem('budget', response.data.budget);
          localStorage.setItem('status', response.data.status);
          this.$router.push('/sponsor-dashboard')
        } else {
          localStorage.setItem('category', response.data.category);
          localStorage.setItem('influencer_id', response.data.influencer_id);
          localStorage.setItem('niche', response.data.niche);
          localStorage.setItem('reach', response.data.reach);
          this.$router.push('/influencer-dashboard')
        }
      }
    })
    .catch(error => {
      if (error.response) {
        if (error.response.status === 401) {
          this.errorMessage = 'Password is incorrect';
        } else if (error.response.status === 404) {
          this.errorMessage = 'Email does not exist';
        } else {
          this.errorMessage = 'An error occurred. Please try again.';
        }
      } else {
        this.errorMessage = 'Network error. Please try again.';
      }
    });
},
    adminLogin() {
      if (this.email === 'admin@adfluence.com' && this.password === 'password') {
      axios.post('http://127.0.0.1:5000/api/login', {
      email: this.email,
      password: this.password
      })
    .then(response => {
      if (response.data.role === 'admin') {
        localStorage.setItem('email', this.email);
        localStorage.setItem('role', response.data.role);
        localStorage.setItem('authToken', response.data.token);
        this.$router.push('/Admin-dashboard');
      } else {
        this.errorMessage = 'Invalid admin credentials';
     }
    })
    .catch(error => {
      console.error('Login error:', error);
      this.errorMessage = 'An error occurred during login';
    });
  }
      else {
        this.errorMessage = 'Invalid admin credentials';
      }
    }
  }
};
</script>

<style>
.login {
  background-color: #f5ebe0;
}

.content {
  display: flex;
  justify-content: center;
  padding: 20px;
}

.card-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.card {
  margin: 20px;
  border-radius: 18px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.info-card {
  background-color: #9f7e69;
  color: white;
  width: 70vw;
}

.form-card {
  background-color: #9f7e69;
  color: white;
  width: 25vw;
  padding: 20px;
}
</style>
