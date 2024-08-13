<template>
  <div class="add-campaign">
    <div class="header-buttons">
      <button @click="navigateTo('/')">Back</button>
      <button @click="logout">Logout</button>
    </div>
    <h2 style="color:#48cae4;font-style:bold;padding-bottom:10px;font-weight:800;font-size:40px;text-shadow: 2px 2px 5px #000;">Edit Campaign {{this.campaign.name}}</h2>
    <form @submit.prevent="submitCampaign">
      <div>
        <label for="name">Campaign Name:</label>
        <input type="text" id="name" v-model="name" required>
      </div>
      <div>
        <label for="description">Description:</label>
        <input id="description" v-model="description" required></input>
      </div>
      <div>
        <label for="start-date">Start Date:</label>
        <input type="date" id="start-date" v-model="start_date" required>
      </div>
      <div>
        <label for="end-date">End Date:</label>
        <input type="date" id="end-date" v-model="end_date" required>
      </div>
      <div>
        <label for="budget">Budget:</label>
        <input type="number" id="budget" v-model="budget" required>
      </div>
      <div>
        <label for="visibility">Visibility:</label>
        <input type="text" id="visibility" v-model="visibility" required>
      </div>
      <div>
        <label for="goals">Goals:</label>
        <input type="text" id="goals" v-model="goals" required>
      </div>
      <button type="submit" @click="updatecampaign(this.id)">Update Campaign</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddCampaign',
  data() {
    return {
      sponsor_id: localStorage.getItem('sponsor_id'),
      name: '',
      description: '',
      start_date: '',
      end_date: '',
      budget: '',
      visibility: '',
      goals: '',
      message: '',
      token:'',
      id:null,
      campaign: [],
    };
  },
  created(){
        this.id =this.$route.params.id;
        this.token=localStorage.getItem('authToken')
        if(!this.token){
            this.$router.push('/login')
        }
        this.fetchCampaign(this.id);
        

    },
  methods: {
    onFileChange(event) {
      this.campaignImg = event.target.files[0];
    },
    fetchCampaign(id) {
      const authToken = localStorage.getItem('authToken');
      axios.get(`http://127.0.0.1:5000/api/campaign/${id}`, {
        headers: {
          'Authorization': authToken,
        },
      })
      .then(response => {
        this.campaign = response.data.data;
        this.name=response.data.data.name;
        this.description=response.data.data.description;
        this.start_date=response.data.data.start_date;
        this.end_date=response.data.data.end_date;
        this.budget=response.data.data.budget;
        this.visibility=response.data.data.visibility;
        this.goals=response.data.data.goals;

      })
      .catch(error => {
        console.error('An error occurred while fetching the campaigns:', error);
      });
    },
    updatecampaign(id) {
      const authToken = localStorage.getItem('authToken');
      if (localStorage.getItem('role') === 'sponsor' || 'admin') {
        axios.put(`http://127.0.0.1:5000/api/campaign/${id}`, 
        {
            name : this.name,
            sponsor_id : this.sponsor_id,
            description : this.description,
            start_date :this.start_date,
            end_date : this.end_date,
            budget : this.budget,
            visibility : this.visibility,
            goals : this.goals
        }
        , {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': authToken,
          },
        })
        .then(response => {
          this.message = 'Campaign added successfully';
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