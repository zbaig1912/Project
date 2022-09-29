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
                <td @click="toggle(row.id)" v-on:click="clickedUserName" >{{ row.name }}</td>
                <td>{{ row.email }}</td>
                <td @click="toggle(row.id)" v-on:click="clickedFirmName">{{ row.firm.name}}</td>
            </tr>
            <tr v-if="tabSelected === 'TRANSACTIONS'" :class="{ opened: opened.includes(row.id) }">
                <td>{{ row.id }}</td>
                <td @click="toggle(row.id)" v-on:click="clickedProductName" >{{ row.product.name }}</td>
                <td>${{ row.total }}</td>
                <td>{{ row.user.name}}</td>
            </tr>
            <tr v-if="opened.includes(row.id)">
                <td colspan="3"><DetailsList :cell="cellClicked" :id="row.id"></DetailsList></td>
            </tr>
        </tbody>
    </table>
</template>


<script>
import axios from 'axios';
import DetailsList from './DetailsList.vue';
export default{
    props: {
        headers: Array,
        tabSelected: String
    },
    components:{DetailsList},
    data() {
        return {
            opened: [],
            rows: [],
            cellClicked: ''
        };
    },
    methods: {
        toggle(id) {
            const index = this.opened.indexOf(id);
            if (index > -1) {
                this.opened.splice(index, 1);
            }
            else {
                this.opened.push(id);
            }
        },
        loadUsers() {
            if (this.tabSelected === "USERS") {
                axios.get("/users/").then(response => {
                    this.rows = response.data;
                });
            }
            if (this.tabSelected === "TRANSACTIONS") {
                axios.get("/trans/").then(response => {
                    this.rows = response.data;
                });
            }
        },
        clickedUserName(){
            this.cellClicked = "UserName";
        },
        clickedFirmName(){
            this.cellClicked = "FirmName";
        },
        clickedProductName(){
            this.cellClicked = "ProductName";
        }
    },
    created() {
        this.loadUsers();
    },
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


