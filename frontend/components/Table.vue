<template >
    <table id="tableComponent" class="table table-bordered table-striped">
        <thead>
            <tr>
                <!-- loop through each value of the fields to get the table header -->
                <th v-for="head in headers" :key='head'> {{head}} </th>
            </tr>
        </thead>
        <tbody v-for="row in rows" >
            <tr v-if="tabSelected === 'USERS'" :class="{ opened: opened.includes(row.id) }">
                <td>{{ row.id }}</td>
                <td @click="toggle(row.id)">{{ row.name }}</td>
                <td>{{ row.email }}</td>
                <td @click="toggle(row.id)">{{ row.firm.name}}</td>
            </tr>
            <tr v-if="tabSelected === 'TRANSACTIONS'" :class="{ opened: opened.includes(row.id) }">
                <td>{{ row.id }}</td>
                <td @click="toggle(row.id)">{{ row.product.name }}</td>
                <td>${{ row.total }}</td>
                <td>{{ row.user.name}}</td>
            </tr>
            <tr v-if="opened.includes(row.id)">
                <td colspan="2">ON!</td>
            </tr>
        </tbody>
    </table>
</template>


<script>
import axios from 'axios';
export default{
    props: {
        headers : Array,
        tabSelected : String
    },
    data() {
        return{
            opened: [],
            rows: []
        }  
    },
    methods: {
        toggle(id) {
            const index = this.opened.indexOf(id);
            if (index > -1) {
                this.opened.splice(index, 1)
            } else {
                this.opened.push(id)
            }
        },
        loadUsers(){
            if(this.tabSelected === 'USERS'){
                axios.get('/users/').then(
                response => {
                this.rows = response.data;
                }
            );   
            }
            if(this.tabSelected === 'TRANSACTIONS'){
                axios.get('/trans/').then(
                response => {
                this.rows = response.data;
                }
            );  
            }
        }
    },
    created(){
        this.loadUsers();
    } 
}
</script>

<style>
table {
  width: 100%;
  border: 1px solid #ccc;
}
td {
  padding: 2px;
  border: 1px solid #ccc;
}
.opened {
  background-color: yellow;
}
</style>


