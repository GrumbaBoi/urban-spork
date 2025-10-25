     
        test_nodes = [n for n in sorted(self.G.nodes(), key=lambda x: (self.G.degree[x], x), reverse=True) if n not in self.vaccinated and n not in self.believed_i]
        test_nodes = test_nodes[:budget]
        # test_nodes = self.rng_test.choice(np.array(list(self.G.nodes)), budget, replace=False)
        for node in test_nodes:
            true = self.model.status[node]         
            r = self.rng_test.random()
            if r <= test_acc_prob:
                obs = true                        
            else:
                # flip s <-> i
                obs = (1 - true) if true in (0, 1) else 2

            if obs == 1:
                self.believed_i.add(node)
            else:
                self.believed_i.discard(node)
                if obs ==0:
                    self.believed_s.add(node)
            
        test_nodes = [n for n in sorted(self.G.nodes(), key=lambda x: (self.G.degree[x], x), reverse=True) if n not in self.vaccinated and n not in self.believed_i]
        test_nodes = test_nodes[:budget]
        for node in test_nodes:
            r = self.rng_test.random()

            if self.model.status[node] == 1 and r <= test_acc_prob:
                self.believed_i.add(node)
                
            elif self.model.status[node] in (0,2) and r > test_acc_prob:
                self.believed_i.add(node)

            if self.model.status[node] != 1 and node in self.believed_i:
                self.believed_i.remove(node)
            
        