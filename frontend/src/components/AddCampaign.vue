<template>
  <div class="add-campaign">
    <h2>Add Campaign</h2>
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
        <input type="date" id="start-date" v-model="startDate" required>
      </div>
      <div>
        <label for="end-date">End Date:</label>
        <input type="date" id="end-date" v-model="endDate" required>
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
      <div>
        <label for="campaign-img">Campaign Image:</label>
        <input type="file" id="campaign-img" @change="onFileChange" required>
      </div>
      <button type="submit">Add Campaign</button>
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
      startDate: '',
      endDate: '',
      budget: '',
      visibility: '',
      goals: '',
      campaignImg: null,
      message: '',
    };
  },
  methods: {
    onFileChange(event) {
      this.campaignImg = event.target.files[0];
    },
    submitCampaign() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('sponsor_id', this.sponsor_id);
      formData.append('description', this.description);
      formData.append('start_date', this.startDate); // Correct the key to match the backend
      formData.append('end_date', this.endDate); // Correct the key to match the backend
      formData.append('budget', this.budget);
      formData.append('visibility', this.visibility);
      formData.append('goals', this.goals);
      formData.append('campaignImg', this.campaignImg);

      const authToken = localStorage.getItem('authToken');
      if (localStorage.getItem('role') === 'sponsor' || 'admin') {
        axios.post('http://127.0.0.1:5000/api/campaign', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': authToken,
          },
        })
        .then(response => {
          alert( "Campaign added successfully, Admin will approve");
          this.$router.push('/sponsor-dashboard');
        })
        .catch(error => {
          console.error(error);
          this.message = error.response ? error.response.data.message : 'An error occurred. Please try again.';
        });
      } else {
        this.message = 'You are not authorized to add a campaign';
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
</style>