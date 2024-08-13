<template>
  <div class="add-campaign">
    <div class="header-buttons">
      <button @click="navigateTo('/')">Back</button>
      <button @click="logout">Logout</button>
    </div>
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">Edit Ad {{this.ad.name}}</h2>
    <form @submit.prevent="submitAd">
      <div>
        <label for="name">Ad Name:</label>
        <input type="text" id="name" v-model="name" required>
      </div>
      <div>
        <label for="content">Content:</label>
        <input id="content" v-model="content" required></input>
      </div>
      <div>
        <label for="start-date">Start Date:</label>
        <input type="date" id="start-date" v-model="start_date" required>
      </div>
      <div>
        <label for="budget">Budget:</label>
        <input type="number" id="budget" v-model="budget" required>
      </div>
      <div>
        <label for="requirements">Requirements:</label>
        <input type="text" id="requirements" v-model="requirements" required>
      </div>
      <div>
        <label for="target_audience">Target audience:</label>
        <input type="text" id="target_audience" v-model="target_audience" required>
      </div>
      <button type="submit" @click="updatead(this.id)">Update Ad</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddAd',
  data() {
    return {
      sponsor_id: localStorage.getItem('sponsor_id'),
      name: '',
      content: '',
      start_date: '',
      budget: '',
      requirements: '',
      target_audience: '',
      message: '',
      token:'',
      id:null,
      ad: [],
    };
  },
  created(){
        this.id =this.$route.params.id;
        this.token=localStorage.getItem('authToken')
        if(!this.token){
            this.$router.push('/login')
        }
        this.fetchad(this.id);
        

    },
  methods: {
    onFileChange(event) {
      this.campaignImg = event.target.files[0];
    },
    fetchad(id) {
      const authToken = localStorage.getItem('authToken');
      axios.get(`http://127.0.0.1:5000/api/Ad/${id}`, {
        headers: {
          'Authorization': authToken,
        },
      })
      .then(response => {
        this.ad = response.data.data;
        this.name=response.data.data.name;
        this.content=response.data.data.content;
        this.start_date=response.data.data.start_date;
        this.budget=response.data.data.budget;
        this.requirements=response.data.data.requirements;
        this.target_audience=response.data.data.target_audience;

      })
      .catch(error => {
        console.error('An error occurred while fetching the campaigns:', error);
      });
    },
    updatead(id) {
      const authToken = localStorage.getItem('authToken');
      if (localStorage.getItem('role') === 'sponsor' || 'admin') {
        axios.put(`http://127.0.0.1:5000/api/Ad/${id}`, 
        {
            name : this.name,
            sponsor_id : this.sponsor_id,
            content : this.content,
            start_date :this.start_date,
            budget : this.budget,
            target_audience : this.target_audience,
            requirements : this.requirements
        }
        , {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': authToken,
          },
        })
        .then(response => {
          this.message = 'Ad updated successfully';
          this.$router.push('/sponsor-dashboard');
        })
        .catch(error => {
          console.error(error);
          this.message = error.response ? error.response.data.message : 'An error occurred. Please try again.';
        });
      } else {
        this.message = 'You are not authorized to update a campaign';
      }
    },
  },
};
</script>

<style>
.add-campaign {
  background-color: #9f7e69;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-size: 13px;
  margin:20px 20px;
}

.add-campaign form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.add-campaign label {
  color: #e3d5ca;
  margin-right:10px
}

.add-campaign input,
.add-campaign textarea {
  padding: 10px;
  border-radius: 5px;
  border: none;
  margin-left:20 px;
}

.add-campaign button {
  padding: 10px 20px;
  border: none;
  border-radius: 18px;
  background-color: #31572c;
  color: #fff;
  cursor: pointer;
}

.add-campaign button:hover {
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