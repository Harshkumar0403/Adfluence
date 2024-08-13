<template>
  <div class="add-ad-container">
     <div class="header-buttons">
      <button @click="navigateTo('/')">Back</button>
      <button @click="logout">Logout</button>
    </div>
    <h3 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">Add New Ad to {{ this.campname }}</h3>
    <form @submit.prevent="submitAd" class="ad-form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" v-model="name" required>
      </div>

      <div class="form-group">
        <label for="content">Content:</label>
        <textarea v-model="content" required></textarea>
      </div>


      <div class="form-group">
        <label for="start_date">Start Date:</label>
        <input type="date" v-model="start_date" required>
      </div>

      <div class="form-group">
        <label for="requirements">Requirements:</label>
        <textarea v-model="requirements" required></textarea>
      </div>

      <div class="form-group">
        <label for="budget">Budget:</label>
        <input type="number" v-model="budget" required>
      </div>

      <div class="form-group">
        <label for="target_audience">Target Audience:</label>
        <input type="text" v-model="target_audience" required>
      </div>


      <button type="submit" class="submit-button" >Submit</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      name: '',
      content: '',
      campaign_id: '',
      campaigns: [],
      sponsor_id: localStorage.getItem('sponsor_id'),
      start_date: '',
      requirements: '',
      budget: '',
      target_audience: '',
      status: true,
      message: '',
      id:null,
      campname:''
    };
  },
  created() {
    this.id =this.$route.params.id;
     this.token=localStorage.getItem('authToken')
        if(!this.token){
            this.$router.push('/login')
        }
    this.fetchCampaigns(this.id);
  },
  methods: {
    fetchCampaigns(id) {
      const authToken = localStorage.getItem('authToken');
      axios.get(`http://127.0.0.1:5000/api/campaign/${id}`, {
        headers: {
          'Authorization': authToken
        }
      })
      .then(response => {
        this.campaigns = response.data.data;
        this.campaign_id=response.data.data.id;
        this.campname=response.data.data.name;
      })
      .catch(error => {
        console.error('Error fetching campaigns:', error);
      });
    },
    onFileChange(event) {
      this.ad_img = event.target.files[0];
    },
    submitAd() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('content', this.content);
      formData.append('campaign_id', this.campaign_id);
      formData.append('sponsor_id', this.sponsor_id);
      formData.append('start_date', this.start_date);
      formData.append('requirements', this.requirements);
      formData.append('budget', this.budget);
      formData.append('target_audience', this.target_audience);
      formData.append('status', this.status === true ? 'true' : 'false');

      const authToken = localStorage.getItem('authToken');
      axios.post('http://127.0.0.1:5000/api/Ad', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': authToken
        }
      })
      .then(response => {
        this.message = 'Ad added successfully';
        this.$router.push('/sponsor-dashboard');
      })
      .catch(error => {
        console.error('Error adding ad:', error);
        this.message = 'An error occurred. Please try again.';
      });
    }
  }
};
</script>

<style scoped>
.add-ad-container {
 background-color: #9f7e69;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-size:  7px;
  margin: 20px 20px;
}

.add-ad-container h2 {
  text-align: center;
  margin-bottom: 20px;
}

.ad-form {
  display: flex;
  flex-direction: column;
  height: 400px;
}

.form-group {
  margin-bottom: 15px;
  
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group textarea {
  resize: vertical;
}

.submit-button {
  padding: 10px 20px;
  border: none;
  border-radius: 18px;
  background-color: #31572c;
  color: #fff;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #e3d5ca;
  color: #31572c;
}
.header-buttons {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
}

.header-buttons button {
  background-color: #31572c;
  color: #fff;
  border: none;
  padding: 10px;
  margin-left: 10px;
  border-radius: 18px;
  cursor: pointer;
}

.header-buttons button:hover {
  background-color: #805a4a;
}
</style>

